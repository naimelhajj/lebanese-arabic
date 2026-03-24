from __future__ import annotations

from pathlib import Path
import xml.etree.ElementTree as ET


SVG_PATH = Path(r"C:\Development\lebanese-arabic\SEO\pages\lesson12\lesson12-family-tree-screenshot-style.svg")
SVG_NS = "http://www.w3.org/2000/svg"
NS = {"svg": SVG_NS}

ET.register_namespace("", SVG_NS)
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")


def float_attr(el: ET.Element, name: str) -> float:
    return float(el.attrib[name])


def main() -> None:
    tree = ET.parse(SVG_PATH)
    root = tree.getroot()

    # Make room for the taller bottom-row cards.
    root.set("height", "720")
    root.set("viewBox", "0 0 1920 720")

    bg = root.find("svg:rect[@id='rect1']", NS)
    if bg is not None:
        bg.set("height", "720")

    changed = []

    for group in root.findall("svg:g", NS):
        rect = group.find("svg:rect", NS)
        if rect is None:
            continue

        shell = None
        core = None
        overlay = None
        translit = None
        arabic = None
        image = None

        for child in list(group):
            tag = child.tag
            classes = child.attrib.get("class", "")
            if tag == f"{{{SVG_NS}}}circle" and "mini-avatar-shell" in classes:
                shell = child
            elif tag == f"{{{SVG_NS}}}circle" and "mini-avatar-core" in classes:
                core = child
            elif tag == f"{{{SVG_NS}}}text" and "mini-avatar-plus" in classes:
                overlay = child
            elif tag == f"{{{SVG_NS}}}text" and "compact-translit" in classes:
                translit = child
            elif tag == f"{{{SVG_NS}}}text" and "compact-arabic" in classes:
                arabic = child
            elif tag == f"{{{SVG_NS}}}image":
                image = child

        if shell is None:
            continue

        x = float_attr(rect, "x")
        y = float_attr(rect, "y")
        width = float_attr(rect, "width")
        center_x = x + (width / 2)
        circle_y = y + 48
        circle_r = 25
        shell_r = 29

        rect.set("height", "112")

        shell.set("class", "avatar-shell")
        shell.set("cx", str(center_x))
        shell.set("cy", str(circle_y))
        shell.set("r", str(shell_r))
        shell.set("style", "fill:none;stroke:rgba(0,0,0,0.15);stroke-width:1.5")

        if core is not None:
            core.set("class", "avatar-core")
            core.set("cx", str(center_x))
            core.set("cy", str(circle_y))
            core.set("r", str(circle_r))

        if overlay is not None:
            overlay.set("class", "avatar-text")
            overlay.set("x", str(center_x))
            overlay.set("y", str(circle_y + 8))
            overlay.text = "+"

        if translit is not None:
            translit.set("class", "compact-translit featured")
            translit.set("x", str(center_x))
            translit.set("y", str(y + 20))

        if arabic is not None:
            arabic.set("class", "compact-arabic featured")
            arabic.set("x", str(center_x))
            arabic.set("y", str(y + 98))

        if image is not None:
            image.set("x", str(center_x - circle_r))
            image.set("y", str(circle_y - circle_r))
            image.set("width", str(circle_r * 2))
            image.set("height", str(circle_r * 2))

            clip_path = image.attrib.get("clip-path", "")
            if clip_path.startswith("url(#") and clip_path.endswith(")"):
                clip_id = clip_path[5:-1]
                clip = root.find(f"svg:defs/svg:clipPath[@id='{clip_id}']/svg:circle", NS)
                if clip is not None:
                    clip.set("cx", str(center_x))
                    clip.set("cy", str(circle_y))
                    clip.set("r", str(circle_r))

        changed.append(group.attrib.get("id", "(no-id)"))

    tree.write(SVG_PATH, encoding="utf-8", xml_declaration=False)
    print(f"Promoted {len(changed)} compact cards:")
    for gid in changed:
        print(f"- {gid}")


if __name__ == "__main__":
    main()
