from __future__ import annotations

from pathlib import Path
import xml.etree.ElementTree as ET


SVG_PATH = Path(r"C:\Development\lebanese-arabic\SEO\pages\lesson12\lesson12-family-tree-screenshot-style.svg")
SVG_NS = "http://www.w3.org/2000/svg"
NS = {"svg": SVG_NS}

ET.register_namespace("", SVG_NS)
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")


MATERNAL_RED = "#ff6a6c"
PATERNAL_WHITE = "#fffdf9"

MATERNAL_GROUPS = {
    "g52",   # left sitteh
    "g54",   # left jeddeh
    "g60",   # mart khaleh
    "g62",   # khaleh
    "g64",   # khalteh
    "g66",   # joz khalteh
    "g68",   # emmeh
    "g80",   # eben khaleh
    "g82",   # bint khaleh
    "g84",   # eben khalteh
    "g86",   # bint khalteh
    "g88",   # mart khayyeh
    "g91",   # khayyeh
    "g116",  # eben khayyeh
    "g118",  # bint khayyeh
}

PATERNAL_GROUPS = {
    "g56",   # right sitteh
    "g58",   # right jeddeh
    "g70",   # bayyeh
    "g72",   # mart 3ammeh
    "g74",   # 3ammeh
    "g76",   # 3amteh
    "g78",   # joz 3amteh
    "g98",   # ekhteh
    "g101",  # joz ekhteh
    "g104",  # eben-3ammeh
    "g106",  # bint 3ammeh
    "g108",  # eben 3amteh
    "g110",  # bint 3amteh
    "g120",  # eben ekhteh
    "g122",  # bint ekhteh
}


def apply_fill(group_id: str, fill: str, root: ET.Element) -> None:
    group = root.find(f"svg:g[@id='{group_id}']", NS)
    if group is None:
        return
    rect = group.find("svg:rect", NS)
    if rect is None:
        return
    rect.set("style", f"fill:{fill};")


def main() -> None:
    tree = ET.parse(SVG_PATH)
    root = tree.getroot()

    for group_id in MATERNAL_GROUPS:
        apply_fill(group_id, MATERNAL_RED, root)

    for group_id in PATERNAL_GROUPS:
        apply_fill(group_id, PATERNAL_WHITE, root)

    tree.write(SVG_PATH, encoding="utf-8", xml_declaration=False)
    print("Applied maternal/paternal branch colors.")


if __name__ == "__main__":
    main()
