from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path


SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)
ET.register_namespace("inkscape", "http://www.inkscape.org/namespaces/inkscape")
ET.register_namespace("sodipodi", "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd")

SVG_PATH = Path(__file__).resolve().parent / "lesson12-family-tree-screenshot-style.svg"


def qname(tag: str) -> str:
    return f"{{{SVG_NS}}}{tag}"


def ensure_style(root: ET.Element) -> None:
    style = root.find(qname("style"))
    if style is None:
        style = ET.SubElement(root, qname("style"))
        style.text = ""
    additions = """
    .mini-avatar-shell { fill: #f7ece3; stroke: rgba(0,0,0,0.12); stroke-width: 1.2; }
    .mini-avatar-core { fill: #6b8d7e; }
    .mini-avatar-plus { font-family: Arial, sans-serif; font-size: 14px; font-weight: 700; fill: #fffaf5; }
    """
    existing = style.text or ""
    if ".mini-avatar-shell" not in existing:
        style.text = existing.rstrip() + "\n" + additions.strip() + "\n"


def add_slots(root: ET.Element) -> None:
    for group in root.findall(qname("g")):
        classes = group.attrib.get("class", "")
        if "compact-card" not in classes:
            continue

        rect = group.find(qname("rect"))
        if rect is None:
            continue

        width = float(rect.attrib.get("width", "0"))
        height = float(rect.attrib.get("height", "0"))
        if width > 112.5 or height > 48:
            continue

        if any(child.attrib.get("class") == "mini-avatar-shell" for child in list(group)):
            continue

        x = float(rect.attrib["x"])
        y = float(rect.attrib["y"])
        center_x = x + 18
        center_y = y + 22

        shell = ET.Element(
            qname("circle"),
            {
                "class": "mini-avatar-shell",
                "cx": str(center_x),
                "cy": str(center_y),
                "r": "13",
            },
        )
        core = ET.Element(
            qname("circle"),
            {
                "class": "mini-avatar-core",
                "cx": str(center_x),
                "cy": str(center_y),
                "r": "10",
            },
        )
        plus = ET.Element(
            qname("text"),
            {
                "class": "mini-avatar-plus",
                "x": str(center_x),
                "y": str(center_y + 5),
                "text-anchor": "middle",
            },
        )
        plus.text = "+"

        insert_at = 1
        group.insert(insert_at, shell)
        group.insert(insert_at + 1, core)
        group.insert(insert_at + 2, plus)

        new_text_x = x + 70
        for child in group.findall(qname("text")):
            child_class = child.attrib.get("class", "")
            if "compact-translit" in child_class and "featured" not in child_class:
                child.set("x", str(new_text_x))
            if "compact-arabic" in child_class and "featured" not in child_class:
                child.set("x", str(new_text_x))


def main() -> None:
    tree = ET.parse(SVG_PATH)
    root = tree.getroot()
    ensure_style(root)
    add_slots(root)
    tree.write(SVG_PATH, encoding="utf-8", xml_declaration=True)
    print(f"Updated {SVG_PATH}")


if __name__ == "__main__":
    main()
