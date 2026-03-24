#!/usr/bin/env python3
"""Fetch raw HTML source for site URLs and save it into this project."""

from __future__ import annotations

import argparse
import fnmatch
import posixpath
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


DEFAULT_TIMEOUT = 30
DEFAULT_USER_AGENT = "Mozilla/5.0 (compatible; SEOSourceScraper/1.0)"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Fetch page source code from a website and save it into the local SEO "
            "project using the existing blogposts/pages folder convention."
        )
    )
    parser.add_argument(
        "urls",
        nargs="*",
        help="One or more page URLs to fetch.",
    )
    parser.add_argument(
        "--urls-file",
        help="Path to a text file with one URL per line.",
    )
    parser.add_argument(
        "--mapping-file",
        help=(
            "Path to a text file mapping URLs to output files. Use one entry per line as "
            "'URL<TAB>relative/output/path' or 'URL,relative/output/path'."
        ),
    )
    parser.add_argument(
        "--base-url",
        default="https://lebanese-arabic.com",
        help="Base site URL used for sitemap defaults and path validation.",
    )
    parser.add_argument(
        "--sitemap-url",
        help=(
            "Sitemap URL to crawl. Defaults to <base-url>/sitemap_index.xml when --sitemap "
            "is used."
        ),
    )
    parser.add_argument(
        "--sitemap",
        action="store_true",
        help="Fetch URLs from the site's sitemap.",
    )
    parser.add_argument(
        "--sitemap-scope",
        choices=["pages-posts", "all"],
        default="pages-posts",
        help=(
            "Which child sitemaps to follow from a sitemap index. 'pages-posts' follows only "
            "WordPress page/post sitemaps. 'all' follows every child sitemap."
        ),
    )
    parser.add_argument(
        "--include",
        action="append",
        default=[],
        help="Only keep URLs matching this wildcard pattern. Can be passed multiple times.",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Skip URLs matching this wildcard pattern. Can be passed multiple times.",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.0,
        help="Seconds to wait between requests.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help="Per-request timeout in seconds.",
    )
    parser.add_argument(
        "--output-root",
        default=".",
        help="Project root where blogposts/ and pages/ live.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing files. By default existing files are skipped.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be written without saving files.",
    )
    parser.add_argument(
        "--user-agent",
        default=DEFAULT_USER_AGENT,
        help="HTTP user agent string to use.",
    )
    return parser.parse_args()


def ensure_trailing_slash(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    path = parsed.path or "/"
    if not path.endswith("/"):
        path += "/"
    return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, path, "", ""))


def normalize_url(url: str) -> str:
    parsed = urllib.parse.urlsplit(url.strip())
    if not parsed.scheme or not parsed.netloc:
        raise ValueError(f"Invalid absolute URL: {url}")
    path = parsed.path or "/"
    normalized = urllib.parse.urlunsplit(
        (parsed.scheme.lower(), parsed.netloc.lower(), path, parsed.query, "")
    )
    return normalized


def slugify_path_segment(segment: str) -> str:
    cleaned = []
    for char in segment.lower():
        if char.isalnum():
            cleaned.append(char)
        elif char in {"-", "_"}:
            cleaned.append("-")
        else:
            cleaned.append("-")
    slug = "".join(cleaned).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug or "home"


def output_path_for_url(url: str, output_root: Path, mapped_output: str | None = None) -> Path:
    if mapped_output:
        mapped_path = Path(mapped_output)
        if mapped_path.is_absolute():
            return mapped_path
        return output_root / mapped_path

    parsed = urllib.parse.urlsplit(url)
    path = parsed.path.strip("/")
    parts = [part for part in path.split("/") if part]

    if not parts:
        slug = "home"
        return output_root / "pages" / slug / f"{slug}-source-code.txt"

    if parts[0] == "blog" and len(parts) >= 2:
        slug = slugify_path_segment(parts[-1])
        return output_root / "blogposts" / f"{slug}-source-code.txt"

    slug = slugify_path_segment(parts[-1])
    return output_root / "pages" / slug / f"{slug}-source-code.txt"


def url_allowed(url: str, base_host: str, includes: list[str], excludes: list[str]) -> bool:
    parsed = urllib.parse.urlsplit(url)
    if parsed.netloc.lower() != base_host.lower():
        return False
    if includes and not any(fnmatch.fnmatch(url, pattern) for pattern in includes):
        return False
    if excludes and any(fnmatch.fnmatch(url, pattern) for pattern in excludes):
        return False
    return True


def fetch_text(url: str, timeout: int, user_agent: str) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        content = response.read()
    return content.decode(charset, errors="replace")


def parse_sitemap(xml_text: str) -> tuple[list[str], list[str]]:
    root = ET.fromstring(xml_text)
    namespace = ""
    if root.tag.startswith("{"):
        namespace = root.tag.split("}", 1)[0] + "}"

    urls: list[str] = []
    child_sitemaps: list[str] = []

    if root.tag == f"{namespace}urlset":
        for loc in root.findall(f".//{namespace}url/{namespace}loc"):
            if loc.text:
                urls.append(loc.text.strip())
    elif root.tag == f"{namespace}sitemapindex":
        for loc in root.findall(f".//{namespace}sitemap/{namespace}loc"):
            if loc.text:
                child_sitemaps.append(loc.text.strip())
    else:
        raise ValueError(f"Unsupported sitemap format: {root.tag}")

    return urls, child_sitemaps


def sitemap_allowed(sitemap_url: str, scope: str) -> bool:
    if scope == "all":
        return True

    path = urllib.parse.urlsplit(sitemap_url).path.lower()
    basename = posixpath.basename(path)
    allowed_patterns = [
        "page-sitemap*.xml",
        "post-sitemap*.xml",
        "page-sitemap.xml",
        "post-sitemap.xml",
    ]
    return any(fnmatch.fnmatch(basename, pattern) for pattern in allowed_patterns)


def collect_sitemap_urls(
    sitemap_url: str,
    timeout: int,
    user_agent: str,
    base_host: str,
    includes: list[str],
    excludes: list[str],
    sitemap_scope: str,
    delay: float,
) -> list[str]:
    pending = [sitemap_url]
    seen_sitemaps: set[str] = set()
    found_urls: list[str] = []
    seen_urls: set[str] = set()

    while pending:
        current = normalize_url(pending.pop(0))
        if current in seen_sitemaps:
            continue
        seen_sitemaps.add(current)

        xml_text = fetch_text(current, timeout=timeout, user_agent=user_agent)
        page_urls, child_sitemaps = parse_sitemap(xml_text)

        for child in child_sitemaps:
            parsed = urllib.parse.urlsplit(child)
            if parsed.netloc.lower() == base_host.lower() and sitemap_allowed(child, sitemap_scope):
                pending.append(child)

        for page_url in page_urls:
            normalized = normalize_url(page_url)
            if normalized in seen_urls:
                continue
            if url_allowed(normalized, base_host, includes, excludes):
                seen_urls.add(normalized)
                found_urls.append(normalized)

        if delay > 0 and pending:
            time.sleep(delay)

    return found_urls


def read_urls_from_file(path: Path) -> list[str]:
    urls: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            urls.append(stripped)
    return urls


def read_mapping_file(path: Path) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        separator = "\t" if "\t" in stripped else ","
        parts = stripped.split(separator, 1)
        if len(parts) != 2:
            raise ValueError(
                f"Invalid mapping on line {line_number}: expected URL and output path"
            )

        url, output_path = parts[0].strip(), parts[1].strip()
        if not url or not output_path:
            raise ValueError(
                f"Invalid mapping on line {line_number}: URL and output path are required"
            )
        mapping[normalize_url(url)] = output_path
    return mapping


def gather_urls(args: argparse.Namespace) -> tuple[list[str], dict[str, str]]:
    urls: list[str] = []
    mapping: dict[str, str] = {}
    if args.urls:
        urls.extend(args.urls)
    if args.urls_file:
        urls.extend(read_urls_from_file(Path(args.urls_file)))
    if args.mapping_file:
        mapping = read_mapping_file(Path(args.mapping_file))
        urls.extend(mapping.keys())

    base_url = ensure_trailing_slash(args.base_url)
    base_host = urllib.parse.urlsplit(base_url).netloc

    if args.sitemap:
        sitemap_url = args.sitemap_url or urllib.parse.urljoin(base_url, "sitemap_index.xml")
        urls.extend(
            collect_sitemap_urls(
                sitemap_url=sitemap_url,
                timeout=args.timeout,
                user_agent=args.user_agent,
                base_host=base_host,
                includes=args.include,
                excludes=args.exclude,
                sitemap_scope=args.sitemap_scope,
                delay=args.delay,
            )
        )

    deduped: list[str] = []
    seen: set[str] = set()
    for raw_url in urls:
        normalized = normalize_url(raw_url)
        if normalized in seen:
            continue
        if url_allowed(normalized, base_host, args.include, args.exclude):
            seen.add(normalized)
            deduped.append(normalized)

    return deduped, mapping


def save_source(url: str, destination: Path, html: str, overwrite: bool) -> str:
    if destination.exists() and not overwrite:
        return "skipped"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(html, encoding="utf-8", newline="\n")
    return "written"


def main() -> int:
    args = parse_args()
    output_root = Path(args.output_root).resolve()

    try:
        urls, mapping = gather_urls(args)
    except Exception as exc:  # pragma: no cover - CLI error path
        print(f"Failed to build URL list: {exc}", file=sys.stderr)
        return 1

    if not urls:
        print("No URLs to process.", file=sys.stderr)
        return 1

    written = 0
    skipped = 0
    failed = 0

    for index, url in enumerate(urls, start=1):
        destination = output_path_for_url(url, output_root, mapping.get(url))
        print(f"[{index}/{len(urls)}] {url}")
        print(f"  -> {destination.relative_to(output_root)}")

        if destination.exists() and not args.overwrite:
            print("  skipped: file exists")
            skipped += 1
            continue

        if args.dry_run:
            print("  dry-run: not fetched")
            continue

        try:
            html = fetch_text(url, timeout=args.timeout, user_agent=args.user_agent)
            result = save_source(url, destination, html, overwrite=args.overwrite)
            if result == "written":
                written += 1
                print("  written")
            else:
                skipped += 1
                print("  skipped")
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError) as exc:
            failed += 1
            print(f"  failed: {exc}", file=sys.stderr)

        if args.delay > 0 and index < len(urls):
            time.sleep(args.delay)

    print(
        f"Done. written={written} skipped={skipped} failed={failed} total={len(urls)}"
    )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
