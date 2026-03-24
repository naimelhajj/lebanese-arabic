from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path


SVG_NS = "http://www.w3.org/2000/svg"
XLINK_NS = "http://www.w3.org/1999/xlink"
ET.register_namespace("", SVG_NS)
ET.register_namespace("xlink", XLINK_NS)
ET.register_namespace("inkscape", "http://www.inkscape.org/namespaces/inkscape")
ET.register_namespace("sodipodi", "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd")

SVG_PATH = Path(__file__).resolve().parent / "lesson12-family-tree-screenshot-style.svg"


def qname(ns: str, tag: str) -> str:
    return f"{{{ns}}}{tag}"


def main() -> None:
    tree = ET.parse(SVG_PATH)
    root = tree.getroot()

    defs = root.find(qname(SVG_NS, "defs"))
    if defs is None:
        defs = ET.SubElement(root, qname(SVG_NS, "defs"), {"id": "defs122"})

    source_image = None
    for child in list(root):
        if child.tag == qname(SVG_NS, "image") and child.attrib.get("id") == "image1":
            source_image = child
            break

    if source_image is None:
        raise RuntimeError("Could not find imported Khayyeh image with id='image1'.")

    href = source_image.attrib.get(qname(XLINK_NS, "href")) or source_image.attrib.get("href")
    if not href:
        raise RuntimeError("Imported Khayyeh image is missing href data.")

    root.remove(source_image)

    clip_id = "clip-khayyeh-photo"
    existing_clip = defs.find(f"{qname(SVG_NS, 'clipPath')}[@id='{clip_id}']")
    if existing_clip is not None:
        defs.remove(existing_clip)

    clip = ET.SubElement(defs, qname(SVG_NS, "clipPath"), {"id": clip_id})
    ET.SubElement(
        clip,
        qname(SVG_NS, "circle"),
        {"cx": "762", "cy": "386", "r": "25"},
    )

    khayyeh_group = None
    for group in root.findall(qname(SVG_NS, "g")):
        if group.attrib.get("id") == "g91":
            khayyeh_group = group
            break

    if khayyeh_group is None:
        raise RuntimeError("Could not find Khayyeh card group with id='g91'.")

    for child in list(khayyeh_group):
        if child.attrib.get("id") in {"circle89", "text89"}:
            khayyeh_group.remove(child)

    shell = None
    rect = None
    for child in list(khayyeh_group):
        if child.attrib.get("id") == "circle88":
            shell = child
        if child.attrib.get("id") == "rect88":
            rect = child

    if rect is None or shell is None:
        raise RuntimeError("Khayyeh card is missing expected rect/shell elements.")

    shell.set("style", "fill:none;stroke:rgba(0,0,0,0.15);stroke-width:1.5")

    image_attrs = {
        "id": "image1-khayyeh-clipped",
        "x": "737",
        "y": "361",
        "width": "50",
        "height": "50",
        "preserveAspectRatio": "xMidYMid slice",
        "clip-path": f"url(#{clip_id})",
    }
    image_el = ET.Element(qname(SVG_NS, "image"), image_attrs)
    image_el.set(qname(XLINK_NS, "href"), href)

    rect_index = list(khayyeh_group).index(rect)
    khayyeh_group.insert(rect_index + 1, image_el)

    tree.write(SVG_PATH, encoding="utf-8", xml_declaration=True)
    print(f"Updated {SVG_PATH}")


if __name__ == "__main__":
    main()
