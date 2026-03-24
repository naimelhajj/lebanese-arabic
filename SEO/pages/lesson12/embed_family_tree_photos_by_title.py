from __future__ import annotations

import base64
import mimetypes
import re
from collections import Counter, defaultdict
from pathlib import Path
import xml.etree.ElementTree as ET


SVG_PATH = Path(r"C:\Development\lebanese-arabic\SEO\pages\lesson12\lesson12-family-tree-screenshot-style.svg")
PHOTO_DIR = Path(r"C:\Development\lebanese-arabic\SEO\pages\lesson12\family-tree")
EXTENSIONS = (".png", ".jpg", ".jpeg", ".webp")

SVG_NS = "http://www.w3.org/2000/svg"
XLINK_NS = "http://www.w3.org/1999/xlink"
NS = {"svg": SVG_NS}

ET.register_namespace("", SVG_NS)
ET.register_namespace("xlink", XLINK_NS)


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = text.replace("&", " and ")
    text = text.replace("/", " ")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-{2,}", "-", text).strip("-")


def embed_data_uri(photo_path: Path) -> str:
    mime_type = mimetypes.guess_type(photo_path.name)[0] or "image/png"
    encoded = base64.b64encode(photo_path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


def float_attr(el: ET.Element, name: str) -> float:
    return float(el.attrib[name])


def find_photo_file(slug: str) -> Path | None:
    for ext in EXTENSIONS:
        candidate = PHOTO_DIR / f"{slug}{ext}"
        if candidate.exists():
            return candidate
    return None


def ensure_defs(root: ET.Element) -> ET.Element:
    defs = root.find("svg:defs", NS)
    if defs is None:
        defs = ET.Element(f"{{{SVG_NS}}}defs")
        root.insert(0, defs)
    return defs


def remove_existing_clip(defs: ET.Element, clip_id: str) -> None:
    for clip in list(defs):
        if clip.tag == f"{{{SVG_NS}}}clipPath" and clip.attrib.get("id") == clip_id:
            defs.remove(clip)


def get_direct_children(group: ET.Element, tag: str) -> list[ET.Element]:
    full_tag = f"{{{SVG_NS}}}{tag}"
    return [child for child in list(group) if child.tag == full_tag]


def main() -> None:
    tree = ET.parse(SVG_PATH)
    root = tree.getroot()
    defs = ensure_defs(root)

    groups = []
    for group in root.findall("svg:g", NS):
        title_el = None
        for text_el in get_direct_children(group, "text"):
            classes = text_el.attrib.get("class", "")
            if "compact-translit" in classes:
                title_el = text_el
                break
        if title_el is not None:
            groups.append((group, (title_el.text or "").strip()))

    title_counts = Counter(title for _, title in groups)
    seen = defaultdict(int)
    embedded = []
    expected = []

    for group, title in groups:
        seen[title] += 1
        base_slug = slugify(title)
        slug = f"{base_slug}-{seen[title]}" if title_counts[title] > 1 else base_slug
        expected.append((title, slug))

        photo_path = find_photo_file(slug)
        if photo_path is None:
            continue

        shell = None
        core = None
        overlay_texts = []
        for child in list(group):
            classes = child.attrib.get("class", "")
            if child.tag == f"{{{SVG_NS}}}circle" and "avatar-shell" in classes:
                shell = child
            elif child.tag == f"{{{SVG_NS}}}circle" and "avatar-core" in classes:
                core = child
            elif child.tag == f"{{{SVG_NS}}}text" and (
                "avatar-text" in classes or "mini-avatar-plus" in classes
            ):
                overlay_texts.append(child)

        # Already-customized cards like Khayyeh may no longer have a core circle.
        if shell is None:
            continue

        cx = float_attr(core or shell, "cx")
        cy = float_attr(core or shell, "cy")
        r = float_attr(core, "r") if core is not None else max(float_attr(shell, "r") - 4, 1)
        shell_r = float_attr(shell, "r")

        for child in list(group):
            if child.tag == f"{{{SVG_NS}}}image":
                group.remove(child)
        if core is not None:
            group.remove(core)
        for text_el in overlay_texts:
            if text_el in group:
                group.remove(text_el)

        clip_id = f"clip-photo-{slug}"
        remove_existing_clip(defs, clip_id)
        clip = ET.SubElement(defs, f"{{{SVG_NS}}}clipPath", {"id": clip_id})
        ET.SubElement(
            clip,
            f"{{{SVG_NS}}}circle",
            {"cx": str(cx), "cy": str(cy), "r": str(r)},
        )

        image_el = ET.Element(
            f"{{{SVG_NS}}}image",
            {
                "id": f"image-{slug}",
                "x": str(cx - r),
                "y": str(cy - r),
                "width": str(r * 2),
                "height": str(r * 2),
                "preserveAspectRatio": "xMidYMid slice",
                "clip-path": f"url(#{clip_id})",
                f"{{{XLINK_NS}}}href": embed_data_uri(photo_path),
            },
        )

        rect_index = 0
        children = list(group)
        for i, child in enumerate(children):
            if child.tag == f"{{{SVG_NS}}}rect":
                rect_index = i
                break
        group.insert(rect_index + 1, image_el)

        shell.set(
            "style",
            f"fill:none;stroke:rgba(0,0,0,0.15);stroke-width:{'1.5' if shell_r >= 20 else '1.2'}",
        )

        embedded.append((title, slug, photo_path.name))

    tree.write(SVG_PATH, encoding="utf-8", xml_declaration=False)

    print("Expected filenames:")
    for title, slug in expected:
        print(f"- {title} -> {slug}")
    print("\nEmbedded photos:")
    if embedded:
        for title, slug, filename in embedded:
            print(f"- {title} -> {filename} ({slug})")
    else:
        print("- none found")


if __name__ == "__main__":
    main()
