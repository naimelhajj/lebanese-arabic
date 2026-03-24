from __future__ import annotations

import base64
from pathlib import Path
import xml.etree.ElementTree as ET


SVG_PATH = Path(r"C:\Development\lebanese-arabic\SEO\pages\lesson12\lesson12-family-tree-screenshot-style.svg")
LOGO_PATH = Path(r"C:\Development\lebanese-arabic\SEO\pages\lesson12\cropped-hiba-logo-without-najem-white.png")
SVG_NS = "http://www.w3.org/2000/svg"
XLINK_NS = "http://www.w3.org/1999/xlink"
NS = {"svg": SVG_NS}

ET.register_namespace("", SVG_NS)
ET.register_namespace("xlink", XLINK_NS)


def svg_el(tag: str, attrs: dict[str, str] | None = None, text: str | None = None) -> ET.Element:
    el = ET.Element(f"{{{SVG_NS}}}{tag}", attrs or {})
    if text is not None:
        el.text = text
    return el


def remove_if_exists(root: ET.Element, element_id: str) -> None:
    target = root.find(f"svg:*[@id='{element_id}']", NS)
    if target is not None:
        root.remove(target)


def main() -> None:
    tree = ET.parse(SVG_PATH)
    root = tree.getroot()

    # Keep accessibility title in sync with the visible graphic title.
    title_el = root.find("svg:title[@id='title2']", NS)
    if title_el is not None:
        title_el.text = "Lebanese Arabic Family Tree"

    remove_if_exists(root, "graphic-heading")
    remove_if_exists(root, "brand-footer")

    heading = svg_el("g", {"id": "graphic-heading"})
    heading.append(
        svg_el(
            "text",
            {
                "x": "60",
                "y": "64",
                "fill": "#fffaf5",
                "font-family": "Arial, sans-serif",
                "font-size": "30",
                "font-weight": "700",
                "letter-spacing": "0.2",
            },
            "Lebanese Arabic Family Tree",
        )
    )
    legend_items = [
        ("Immediate family", "#80c8a9", "#80c8a9"),
        ("Extended family", "#ff6a6c", "#ff6a6c"),
        ("Non-blood", "#d7b276", "#d7b276"),
        ("Me", "#fffdf9", "rgba(255, 250, 245, 0.7)"),
    ]
    start_x = 60
    y = 92
    swatch_w = 18
    swatch_h = 12
    gap_after_swatch = 10
    item_gap = 26
    char_px = 7.1
    cursor_x = start_x
    for label, fill, stroke in legend_items:
        heading.append(
            svg_el(
                "rect",
                {
                    "x": str(cursor_x),
                    "y": str(y - 10),
                    "width": str(swatch_w),
                    "height": str(swatch_h),
                    "rx": "4",
                    "ry": "4",
                    "fill": fill,
                    "stroke": stroke,
                    "stroke-width": "1.2",
                },
            )
        )
        text_x = cursor_x + swatch_w + gap_after_swatch
        heading.append(
            svg_el(
                "text",
                {
                    "x": str(text_x),
                    "y": str(y),
                    "fill": "#f7ece3",
                    "font-family": "Arial, sans-serif",
                    "font-size": "13",
                    "font-weight": "600",
                },
                label,
            )
        )
        cursor_x = text_x + int(len(label) * char_px) + item_gap

    logo_data = base64.b64encode(LOGO_PATH.read_bytes()).decode("ascii")
    footer = svg_el("g", {"id": "brand-footer"})
    footer.append(
        svg_el(
            "rect",
            {
                "x": "1450",
                "y": "660",
                "width": "410",
                "height": "56",
                "rx": "16",
                "ry": "16",
                "fill": "rgba(12, 36, 31, 0.28)",
                "stroke": "rgba(255, 250, 245, 0.18)",
                "stroke-width": "1",
            },
        )
    )
    footer.append(
        svg_el(
            "image",
            {
                "id": "brand-footer-logo",
                "x": "1470",
                "y": "672",
                "width": "32",
                "height": "32",
                f"{{{XLINK_NS}}}href": f"data:image/png;base64,{logo_data}",
            },
        )
    )
    footer.append(
        svg_el(
            "text",
            {
                "x": "1516",
                "y": "686",
                "fill": "#fffaf5",
                "font-family": "Arial, sans-serif",
                "font-size": "16",
                "font-weight": "700",
            },
            "Lebanese Arabic with Hiba",
        )
    )
    footer.append(
        svg_el(
            "text",
            {
                "x": "1516",
                "y": "703",
                "fill": "#f7ece3",
                "font-family": "Arial, sans-serif",
                "font-size": "12",
                "font-weight": "600",
            },
            "lebanese-arabic.com",
        )
    )

    root.append(heading)
    root.append(footer)

    tree.write(SVG_PATH, encoding="utf-8", xml_declaration=False)
    print("Added SVG title and brand footer.")


if __name__ == "__main__":
    main()
