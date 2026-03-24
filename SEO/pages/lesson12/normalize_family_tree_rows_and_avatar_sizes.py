from __future__ import annotations

from pathlib import Path
import xml.etree.ElementTree as ET


SVG_PATH = Path(r"C:\Development\lebanese-arabic\SEO\pages\lesson12\lesson12-family-tree-screenshot-style.svg")
SVG_NS = "http://www.w3.org/2000/svg"
NS = {"svg": SVG_NS}

ET.register_namespace("", SVG_NS)
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")


ROW_TARGETS = {
    10.0: 10.0,
    204.0: 204.0,
    338.0: 398.0,
    398.0: 398.0,
    592.0: 592.0,
}

CARD_HEIGHT = 120.0
TRANSLIT_Y_OFFSET = 18.0
CIRCLE_Y_OFFSET = 56.0
SHELL_R = 34.0
PHOTO_R = 30.0
ARABIC_Y_OFFSET = 110.0


def float_attr(el: ET.Element, name: str) -> float:
    return float(el.attrib[name])


def update_card_group(root: ET.Element, group: ET.Element) -> None:
    rect = group.find("svg:rect", NS)
    if rect is None:
        return

    y = float_attr(rect, "y")
    if y not in ROW_TARGETS:
        return

    x = float_attr(rect, "x")
    width = float_attr(rect, "width")
    target_y = ROW_TARGETS[y]
    center_x = x + (width / 2)
    circle_y = target_y + CIRCLE_Y_OFFSET

    rect.set("y", str(target_y))
    rect.set("height", str(CARD_HEIGHT))

    for child in list(group):
        tag = child.tag
        classes = child.attrib.get("class", "")

        if tag == f"{{{SVG_NS}}}circle" and ("avatar-shell" in classes or "mini-avatar-shell" in classes):
            child.set("class", "avatar-shell")
            child.set("cx", str(center_x))
            child.set("cy", str(circle_y))
            child.set("r", str(SHELL_R))
            child.set("style", "fill:none;stroke:rgba(0,0,0,0.15);stroke-width:1.5")

        elif tag == f"{{{SVG_NS}}}circle" and ("avatar-core" in classes or "mini-avatar-core" in classes):
            child.set("class", "avatar-core")
            child.set("cx", str(center_x))
            child.set("cy", str(circle_y))
            child.set("r", str(PHOTO_R))

        elif tag == f"{{{SVG_NS}}}text" and ("avatar-text" in classes or "mini-avatar-plus" in classes):
            child.set("class", "avatar-text")
            child.set("x", str(center_x))
            child.set("y", str(circle_y + 8))
            child.text = "+"

        elif tag == f"{{{SVG_NS}}}text" and "compact-translit" in classes:
            child.set("class", "compact-translit featured")
            child.set("x", str(center_x))
            child.set("y", str(target_y + TRANSLIT_Y_OFFSET))

        elif tag == f"{{{SVG_NS}}}text" and "compact-arabic" in classes:
            child.set("class", "compact-arabic featured")
            child.set("x", str(center_x))
            child.set("y", str(target_y + ARABIC_Y_OFFSET))

        elif tag == f"{{{SVG_NS}}}image":
            child.set("x", str(center_x - PHOTO_R))
            child.set("y", str(circle_y - PHOTO_R))
            child.set("width", str(PHOTO_R * 2))
            child.set("height", str(PHOTO_R * 2))

            clip_path = child.attrib.get("clip-path", "")
            if clip_path.startswith("url(#") and clip_path.endswith(")"):
                clip_id = clip_path[5:-1]
                clip = root.find(f"svg:defs/svg:clipPath[@id='{clip_id}']/svg:circle", NS)
                if clip is not None:
                    clip.set("cx", str(center_x))
                    clip.set("cy", str(circle_y))
                    clip.set("r", str(PHOTO_R))


def set_line_y(root: ET.Element, line_id: str, y: float) -> None:
    line = root.find(f"svg:line[@id='{line_id}']", NS)
    if line is None:
        return
    line.set("y1", str(y))
    line.set("y2", str(y))


def set_line_y2(root: ET.Element, line_id: str, y2: float) -> None:
    line = root.find(f"svg:line[@id='{line_id}']", NS)
    if line is None:
        return
    line.set("y2", str(y2))


def main() -> None:
    tree = ET.parse(SVG_PATH)
    root = tree.getroot()

    root.set("height", "740")
    root.set("viewBox", "0 0 1920 740")

    bg = root.find("svg:rect[@id='rect1']", NS)
    if bg is not None:
        bg.set("height", "740")

    for group in root.findall("svg:g", NS):
        update_card_group(root, group)

    # Couple lines centered on each row after the card height increase.
    for line_id in ("line13-5-7", "line13-5"):
        set_line_y(root, line_id, 66.0)
    for line_id in ("line11", "line12", "line13", "line14", "line15"):
        set_line_y(root, line_id, 260.0)
    for line_id in ("line21", "line22", "line23"):
        set_line_y(root, line_id, 454.0)

    # Bring previously split third-generation branches onto the same row.
    for line_id in ("line18", "line20", "line46"):
        set_line_y2(root, line_id, 398.0)

    tree.write(SVG_PATH, encoding="utf-8", xml_declaration=False)
    print("Normalized card rows and avatar sizes.")


if __name__ == "__main__":
    main()
