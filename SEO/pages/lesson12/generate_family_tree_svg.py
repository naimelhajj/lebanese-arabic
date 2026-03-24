from __future__ import annotations

import base64
import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "My-Family-21-Mar-2026-134318836.csv"
TXT_PATH = BASE_DIR / "My-Family-21-Mar-2026-134326526.txt"
SVG_PATH = BASE_DIR / "lesson12-family-tree.svg"
SCREENSHOT_STYLE_SVG_PATH = BASE_DIR / "lesson12-family-tree-screenshot-style.svg"
PHOTOS_DIR = BASE_DIR / "family-tree-photos"


@dataclass
class Person:
    person_id: str
    given_name: str
    full_name: str
    gender: str
    mother_id: str
    father_id: str
    partner_id: str
    translit: str
    arabic: str
    gloss: str


CARD_W = 220
CARD_H = 108
PANEL_W = 1120
PANEL_H = 940


GLOSS_BY_ID = {
    "TAV32": "daughter",
    "POXJI": "son",
    "MDG4X": "sister",
    "HFYF5": "brother's wife",
    "M6OLG": "spouse",
    "SY510": "sister's son",
    "SW73F": "brother's son",
    "V07RX": "maternal aunt's son",
    "CBUPO": "maternal uncle's son",
    "G4T20": "paternal aunt's son",
    "OER1D": "paternal uncle's son",
    "VQYK9": "mother",
    "START": "me",
    "MC8ND": "sister's daughter",
    "YO9NZ": "brother's daughter",
    "GD8CH": "maternal aunt's daughter",
    "EXAY8": "maternal uncle's daughter",
    "X06TU": "paternal aunt's daughter",
    "OR4CF": "paternal uncle's daughter",
    "IW8LA": "father",
    "N7KUB": "maternal grandfather",
    "NECA6": "paternal grandfather",
    "UW810": "sister's husband",
    "OTMR8": "maternal aunt's husband",
    "ZWNPD": "paternal aunt's husband",
    "R69PZ": "maternal aunt",
    "Q2R2G": "maternal uncle",
    "EPTAW": "brother",
    "LXPV4": "maternal grandmother",
    "DD56C": "paternal grandmother",
    "UTEGJ": "paternal aunt",
    "KOHKZ": "paternal uncle",
    "SZKMD": "maternal uncle's wife",
    "G6AQX": "paternal uncle's wife",
}


OVERRIDE_TRANSLIT = {
    "M6OLG": "Marteh / Jawzeh",
    "HFYF5": "Mart Khayyeh",
    "UW810": "Joz Ekhteh",
    "OTMR8": "Joz Khalteh",
    "ZWNPD": "Joz 3amteh",
    "SZKMD": "Mart Khaleh",
    "G6AQX": "Mart 3ammeh",
}


OVERRIDE_ARABIC = {
    "TAV32": "بنتي",
    "POXJI": "ابني",
    "MDG4X": "أختي",
    "HFYF5": "مرت خيي",
    "M6OLG": "مرتي / جوزي",
}


IMMEDIATE_POSITIONS = {
    "VQYK9": (860, 110),
    "IW8LA": (1120, 110),
    "MDG4X": (240, 315),
    "UW810": (500, 315),
    "START": (860, 315),
    "M6OLG": (1120, 315),
    "EPTAW": (1500, 315),
    "HFYF5": (1760, 315),
    "MC8ND": (160, 540),
    "SY510": (420, 540),
    "TAV32": (860, 540),
    "POXJI": (1120, 540),
    "YO9NZ": (1420, 540),
    "SW73F": (1680, 540),
}


MATERNAL_POSITIONS = {
    "LXPV4": (140, 110),
    "N7KUB": (400, 110),
    "R69PZ": (20, 320),
    "OTMR8": (250, 320),
    "VQYK9": (450, 320),
    "Q2R2G": (650, 320),
    "SZKMD": (880, 320),
    "GD8CH": (20, 560),
    "V07RX": (250, 560),
    "EXAY8": (650, 560),
    "CBUPO": (880, 560),
}


PATERNAL_POSITIONS = {
    "DD56C": (140, 110),
    "NECA6": (400, 110),
    "UTEGJ": (20, 320),
    "ZWNPD": (250, 320),
    "IW8LA": (450, 320),
    "KOHKZ": (650, 320),
    "G6AQX": (880, 320),
    "X06TU": (20, 560),
    "G4T20": (250, 560),
    "OR4CF": (650, 560),
    "OER1D": (880, 560),
}


def read_csv_people() -> dict[str, Person]:
    people: dict[str, Person] = {}
    with CSV_PATH.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            person_id = row["ID"]
            given_name = row["Given names"].strip()
            full_name = row["Full name"].strip()
            translit, arabic = split_name(given_name, full_name)
            people[person_id] = Person(
                person_id=person_id,
                given_name=given_name,
                full_name=full_name,
                gender=row["Gender"].strip().lower(),
                mother_id=row["Mother ID"].strip(),
                father_id=row["Father ID"].strip(),
                partner_id=row["Partner ID"].strip(),
                translit=OVERRIDE_TRANSLIT.get(person_id, translit),
                arabic=OVERRIDE_ARABIC.get(person_id, arabic),
                gloss=GLOSS_BY_ID.get(person_id, ""),
            )
    return people


def split_name(given_name: str, full_name: str) -> tuple[str, str]:
    translit = given_name or full_name
    arabic_match = re.search(r"[\u0600-\u06FF].*$", full_name)
    arabic = arabic_match.group(0).strip() if arabic_match else ""
    return translit.strip(), arabic


def read_txt_names() -> set[str]:
    names: set[str] = set()
    for line in TXT_PATH.read_text(encoding="utf-8").splitlines():
        if line.startswith("Full name:"):
            names.add(line.split(":", 1)[1].strip())
    return names


def gender_class(person: Person) -> str:
    if person.gender == "female":
        return "female"
    if person.gender == "male":
        return "male"
    return "neutral"


def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def wrap_words(text: str, max_chars: int = 14) -> list[str]:
    parts = [part for part in re.split(r"(\s+|-)", text) if part]
    lines: list[str] = []
    current = ""
    for part in parts:
        candidate = f"{current}{part}"
        if current and len(candidate.replace(" ", "")) > max_chars:
            lines.append(current.strip())
            current = part.strip()
        else:
            current = candidate
    if current.strip():
        lines.append(current.strip())
    return lines[:2]


def card_svg(person: Person, x: int, y: int) -> str:
    cx = x + CARD_W / 2
    lines = [
        f'<g class="card {gender_class(person)}">',
        f'  <rect x="{x}" y="{y}" rx="20" ry="20" width="{CARD_W}" height="{CARD_H}" />',
        f'  <circle class="badge" cx="{x + 34}" cy="{y + 30}" r="18" />',
        f'  <text class="badge-text" x="{x + 34}" y="{y + 37}" text-anchor="middle">{esc((person.translit[:1] or "?").upper())}</text>',
        f'  <text class="translit" x="{cx}" y="{y + 33}" text-anchor="middle">{esc(person.translit)}</text>',
    ]
    if person.arabic:
        lines.append(
            f'  <text class="arabic" x="{cx}" y="{y + 60}" text-anchor="middle" direction="rtl">{esc(person.arabic)}</text>'
        )
        gloss_y = y + 86
    else:
        gloss_y = y + 67
    if person.gloss:
        lines.append(
            f'  <text class="gloss" x="{cx}" y="{gloss_y}" text-anchor="middle">{esc(person.gloss)}</text>'
        )
    lines.append("</g>")
    return "\n".join(lines)


def compact_card_svg(person: Person, x: int, y: int, w: int = 112, h: int = 44, featured: bool = False) -> str:
    if featured:
        w, h = 116, 112
    rect_class = "compact-card female" if gender_class(person) == "female" else "compact-card male"
    lines = [f'<g class="{rect_class}">', f'  <rect x="{x}" y="{y}" rx="10" ry="10" width="{w}" height="{h}" />']
    translit_lines = wrap_words(person.translit, 12 if featured else 14)

    if featured:
        avatar_cx = x + w / 2
        avatar_cy = y + 48
        photo_href = photo_data_uri(person.person_id)
        lines.extend(
            [
                f'  <circle class="avatar-shell" cx="{avatar_cx}" cy="{avatar_cy}" r="29" />',
            ]
        )
        if photo_href:
            clip_id = f"avatar-{person.person_id}"
            lines.extend(
                [
                    f'  <clipPath id="{clip_id}"><circle cx="{avatar_cx}" cy="{avatar_cy}" r="25" /></clipPath>',
                    f'  <image href="{photo_href}" x="{avatar_cx - 25}" y="{avatar_cy - 25}" width="50" height="50" preserveAspectRatio="xMidYMid slice" clip-path="url(#{clip_id})" />',
                ]
            )
        else:
            lines.extend(
                [
                    f'  <circle class="avatar-core" cx="{avatar_cx}" cy="{avatar_cy}" r="25" />',
                    f'  <text class="avatar-text" x="{avatar_cx}" y="{avatar_cy + 8}" text-anchor="middle">{esc((person.translit[:1] or "?").upper())}</text>',
                ]
            )
        title_y = y + 20
        for index, line in enumerate(translit_lines):
            lines.append(
                f'  <text class="compact-translit featured" x="{x + w / 2}" y="{title_y + index * 14}" text-anchor="middle">{esc(line)}</text>'
            )
        if person.arabic:
            lines.append(
                f'  <text class="compact-arabic featured" x="{x + w / 2}" y="{y + 98}" text-anchor="middle" direction="rtl">{esc(person.arabic)}</text>'
            )
    else:
        base_y = y + 18
        for index, line in enumerate(translit_lines):
            lines.append(
                f'  <text class="compact-translit" x="{x + w / 2}" y="{base_y + index * 12}" text-anchor="middle">{esc(line)}</text>'
            )
        if person.arabic:
            arabic_y = y + (34 if len(translit_lines) == 1 else 38)
            lines.append(
                f'  <text class="compact-arabic" x="{x + w / 2}" y="{arabic_y}" text-anchor="middle" direction="rtl">{esc(person.arabic)}</text>'
            )
    lines.append("</g>")
    return "\n".join(lines)


def couple_line(a: tuple[int, int], b: tuple[int, int]) -> str:
    ax = a[0] + CARD_W
    ay = a[1] + CARD_H / 2
    bx = b[0]
    by = b[1] + CARD_H / 2
    return f'<line class="couple" x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" />'


def sibling_connector(parents: tuple[tuple[int, int], tuple[int, int]], children: Iterable[tuple[int, int]]) -> str:
    px = (parents[0][0] + parents[1][0] + CARD_W) / 2
    parent_y = parents[0][1] + CARD_H
    child_centers = [(x + CARD_W / 2, y) for x, y in children]
    line_y = min(y for _, y in child_centers) - 34
    left_x = min(x for x, _ in child_centers)
    right_x = max(x for x, _ in child_centers)
    parts = [
        f'<line class="family" x1="{px}" y1="{parent_y}" x2="{px}" y2="{line_y}" />',
        f'<line class="family" x1="{left_x}" y1="{line_y}" x2="{right_x}" y2="{line_y}" />',
    ]
    for cx, cy in child_centers:
        parts.append(f'<line class="family" x1="{cx}" y1="{line_y}" x2="{cx}" y2="{cy}" />')
    return "\n".join(parts)


def children_connector(couple: tuple[tuple[int, int], tuple[int, int]], children: Iterable[tuple[int, int]]) -> str:
    center_x = (couple[0][0] + couple[1][0] + CARD_W) / 2
    start_y = couple[0][1] + CARD_H / 2
    child_centers = [(x + CARD_W / 2, y) for x, y in children]
    line_y = min(y for _, y in child_centers) - 34
    left_x = min(x for x, _ in child_centers)
    right_x = max(x for x, _ in child_centers)
    parts = [
        f'<line class="family" x1="{center_x}" y1="{start_y}" x2="{center_x}" y2="{line_y}" />',
        f'<line class="family" x1="{left_x}" y1="{line_y}" x2="{right_x}" y2="{line_y}" />',
    ]
    for cx, cy in child_centers:
        parts.append(f'<line class="family" x1="{cx}" y1="{line_y}" x2="{cx}" y2="{cy}" />')
    return "\n".join(parts)


def panel_frame(x: int, y: int, width: int, height: int, title: str, subtitle: str = "") -> str:
    parts = [
        f'<g class="panel-frame">',
        f'  <rect x="{x}" y="{y}" width="{width}" height="{height}" rx="28" ry="28" />',
        f'  <text class="panel-title" x="{x + 34}" y="{y + 54}">{esc(title)}</text>',
    ]
    if subtitle:
        parts.append(f'  <text class="panel-subtitle" x="{x + 34}" y="{y + 84}">{esc(subtitle)}</text>')
    parts.append("</g>")
    return "\n".join(parts)


def panel_group(people: dict[str, Person], positions: dict[str, tuple[int, int]], origin_x: int, origin_y: int) -> str:
    return "\n".join(
        card_svg(people[person_id], origin_x + x, origin_y + y)
        for person_id, (x, y) in positions.items()
    )


def build_svg() -> str:
    people = read_csv_people()
    txt_names = read_txt_names()
    csv_names = {p.full_name for p in people.values()}
    overlap = len(csv_names & txt_names)
    if overlap < 20:
        raise RuntimeError("TXT export does not match CSV export closely enough to trust the build.")

    width = 2440
    height = 1780
    top_x, top_y = 60, 60
    top_w, top_h = 2320, 660
    left_x, left_y = 60, 780
    right_x, right_y = 1260, 780

    top_positions = {person_id: (top_x + x, top_y + y) for person_id, (x, y) in IMMEDIATE_POSITIONS.items()}
    left_positions = {person_id: (left_x + x, left_y + y) for person_id, (x, y) in MATERNAL_POSITIONS.items()}
    right_positions = {person_id: (right_x + x, right_y + y) for person_id, (x, y) in PATERNAL_POSITIONS.items()}

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '  <title id="title">Lebanese Arabic family tree vocabulary chart</title>',
        '  <desc id="desc">A first-party SVG family tree built from local CSV and plain-text exports for lesson 12. It maps Lebanese Arabic family terms across immediate, maternal, and paternal branches.</desc>',
        "  <defs>",
        '    <linearGradient id="bg" x1="0" x2="1" y1="0" y2="1">',
        '      <stop offset="0%" stop-color="#fcfaf6" />',
        '      <stop offset="100%" stop-color="#f2ede5" />',
        "    </linearGradient>",
        "  </defs>",
        "  <style>",
        "    .bg { fill: url(#bg); }",
        "    .header { font-family: Georgia, 'Times New Roman', serif; font-size: 42px; font-weight: 700; fill: #2c241f; }",
        "    .subheader { font-family: Arial, sans-serif; font-size: 18px; fill: #6e5a50; }",
        "    .panel-frame rect { fill: rgba(255,255,255,0.72); stroke: #ccbfae; stroke-width: 2; }",
        "    .panel-title { font-family: Georgia, 'Times New Roman', serif; font-size: 28px; font-weight: 700; fill: #3d322b; }",
        "    .panel-subtitle { font-family: Arial, sans-serif; font-size: 15px; fill: #7a665d; }",
        "    .card rect { stroke-width: 2; }",
        "    .card.female rect { fill: #fff4f0; stroke: #d9a9a2; }",
        "    .card.male rect { fill: #f2f7fb; stroke: #9eb8cf; }",
        "    .card.neutral rect { fill: #f8f1e7; stroke: #cfbb9c; }",
        "    .badge { fill: rgba(255,255,255,0.95); stroke: rgba(0,0,0,0.08); stroke-width: 1.4; }",
        "    .badge-text { font-family: Arial, sans-serif; font-size: 17px; font-weight: 700; fill: #5a4a42; }",
        "    .translit { font-family: Arial, sans-serif; font-size: 18px; font-weight: 700; fill: #2c241f; }",
        "    .arabic { font-family: 'Noto Naskh Arabic', 'Amiri', serif; font-size: 22px; fill: #46372f; }",
        "    .gloss { font-family: Arial, sans-serif; font-size: 14px; fill: #7a665d; }",
        "    .family { stroke: #8d796d; stroke-width: 3; fill: none; stroke-linecap: round; }",
        "    .couple { stroke: #b39b8c; stroke-width: 4; fill: none; stroke-linecap: round; }",
        "    .footer { font-family: Arial, sans-serif; font-size: 14px; fill: #7b675d; }",
        "  </style>",
        f'  <rect class="bg" x="0" y="0" width="{width}" height="{height}" />',
        '  <text class="header" x="60" y="54">Lebanese Arabic Family Tree</text>',
        '  <text class="subheader" x="60" y="84">First-party SVG built from the local CSV and plain-text exports for Lesson 12.</text>',
        f"  {panel_frame(top_x, top_y, top_w, top_h, 'Immediate Family', 'Central family terms and close relatives')}",
        f"  {panel_frame(left_x, left_y, PANEL_W, PANEL_H, 'Maternal Side', 'Relatives connected through mother')}",
        f"  {panel_frame(right_x, right_y, PANEL_W, PANEL_H, 'Paternal Side', 'Relatives connected through father')}",
    ]

    # Immediate family connectors
    lines.extend(
        [
            couple_line(top_positions["VQYK9"], top_positions["IW8LA"]),
            sibling_connector(
                (top_positions["VQYK9"], top_positions["IW8LA"]),
                [top_positions["MDG4X"], top_positions["START"], top_positions["EPTAW"]],
            ),
            couple_line(top_positions["MDG4X"], top_positions["UW810"]),
            couple_line(top_positions["START"], top_positions["M6OLG"]),
            couple_line(top_positions["EPTAW"], top_positions["HFYF5"]),
            children_connector(
                (top_positions["MDG4X"], top_positions["UW810"]),
                [top_positions["MC8ND"], top_positions["SY510"]],
            ),
            children_connector(
                (top_positions["START"], top_positions["M6OLG"]),
                [top_positions["TAV32"], top_positions["POXJI"]],
            ),
            children_connector(
                (top_positions["EPTAW"], top_positions["HFYF5"]),
                [top_positions["YO9NZ"], top_positions["SW73F"]],
            ),
        ]
    )

    # Maternal side connectors
    lines.extend(
        [
            couple_line(left_positions["LXPV4"], left_positions["N7KUB"]),
            sibling_connector(
                (left_positions["LXPV4"], left_positions["N7KUB"]),
                [left_positions["R69PZ"], left_positions["VQYK9"], left_positions["Q2R2G"]],
            ),
            couple_line(left_positions["R69PZ"], left_positions["OTMR8"]),
            couple_line(left_positions["Q2R2G"], left_positions["SZKMD"]),
            children_connector(
                (left_positions["R69PZ"], left_positions["OTMR8"]),
                [left_positions["GD8CH"], left_positions["V07RX"]],
            ),
            children_connector(
                (left_positions["Q2R2G"], left_positions["SZKMD"]),
                [left_positions["EXAY8"], left_positions["CBUPO"]],
            ),
        ]
    )

    # Paternal side connectors
    lines.extend(
        [
            couple_line(right_positions["DD56C"], right_positions["NECA6"]),
            sibling_connector(
                (right_positions["DD56C"], right_positions["NECA6"]),
                [right_positions["UTEGJ"], right_positions["IW8LA"], right_positions["KOHKZ"]],
            ),
            couple_line(right_positions["UTEGJ"], right_positions["ZWNPD"]),
            couple_line(right_positions["KOHKZ"], right_positions["G6AQX"]),
            children_connector(
                (right_positions["UTEGJ"], right_positions["ZWNPD"]),
                [right_positions["X06TU"], right_positions["G4T20"]],
            ),
            children_connector(
                (right_positions["KOHKZ"], right_positions["G6AQX"]),
                [right_positions["OR4CF"], right_positions["OER1D"]],
            ),
        ]
    )

    lines.append(panel_group(people, IMMEDIATE_POSITIONS, top_x, top_y))
    lines.append(panel_group(people, MATERNAL_POSITIONS, left_x, left_y))
    lines.append(panel_group(people, PATERNAL_POSITIONS, right_x, right_y))
    lines.extend(
        [
            '  <text class="footer" x="60" y="1760">Photos are not embedded in this version because the CSV and TXT exports do not include stable photo references.</text>',
            "</svg>",
        ]
    )
    return "\n".join(lines)


def build_screenshot_style_svg() -> str:
    people = read_csv_people()
    txt_names = read_txt_names()
    if len({p.full_name for p in people.values()} & txt_names) < 20:
        raise RuntimeError("TXT export does not match CSV export closely enough to trust the build.")

    width = 1920
    height = 652

    positions = {
        "LXPV4": (702, 10, False),
        "N7KUB": (854, 10, False),
        "DD56C": (964, 10, False),
        "NECA6": (1116, 10, False),
        "SZKMD": (52, 204, False),
        "Q2R2G": (182, 204, False),
        "R69PZ": (312, 204, False),
        "OTMR8": (442, 204, False),
        "VQYK9": (834, 204, False),
        "IW8LA": (964, 204, False),
        "G6AQX": (1352, 204, False),
        "KOHKZ": (1482, 204, False),
        "UTEGJ": (1612, 204, False),
        "ZWNPD": (1742, 204, False),
        "CBUPO": (52, 398, False),
        "EXAY8": (182, 398, False),
        "V07RX": (312, 398, False),
        "GD8CH": (442, 398, False),
        "HFYF5": (574, 398, False),
        "EPTAW": (704, 338, True),
        "M6OLG": (834, 398, False),
        "START": (964, 398, False),
        "MDG4X": (1094, 338, True),
        "UW810": (1224, 338, True),
        "OER1D": (1354, 338, True),
        "OR4CF": (1484, 398, False),
        "G4T20": (1614, 398, False),
        "X06TU": (1744, 398, False),
        "POXJI": (834, 592, False),
        "TAV32": (964, 592, False),
        "SW73F": (574, 592, False),
        "YO9NZ": (704, 592, False),
        "SY510": (1094, 592, False),
        "MC8ND": (1224, 592, False),
    }

    def card_dims(person_id: str) -> tuple[int, int]:
        _, _, featured = positions[person_id]
        if featured:
            return 116, 112
        return 112, 44

    def normal_center(person_id: str) -> tuple[float, float]:
        x, y, featured = positions[person_id]
        if featured:
            return x + 58, y + 56
        return x + 56, y + 22

    def side_anchor(person_id: str, side: str, y_override: float | None = None) -> tuple[float, float]:
        x, y, _ = positions[person_id]
        w, h = card_dims(person_id)
        anchor_y = y_override if y_override is not None else y + h / 2
        if side == "left":
            return x, anchor_y
        return x + w, anchor_y

    def top_of(person_id: str) -> tuple[float, float]:
        x, y, _ = positions[person_id]
        return x + 56, y

    def bottom_of(person_id: str) -> tuple[float, float]:
        x, y, featured = positions[person_id]
        return x + 56, y + (112 if featured else 44)

    def couple_line_compact(a: str, b: str) -> str:
        _, ay = normal_center(a)
        _, by = normal_center(b)
        line_y = max(ay, by)
        ax, _ = side_anchor(a, "right", line_y)
        bx, _ = side_anchor(b, "left", line_y)
        return f'<line class="compact-couple" x1="{ax}" y1="{line_y}" x2="{bx}" y2="{line_y}" />'

    def sibling_bus(parent_a: str, parent_b: str, children: list[str], drop: int = 30) -> str:
        px = (normal_center(parent_a)[0] + normal_center(parent_b)[0]) / 2
        py = bottom_of(parent_a)[1]
        line_y = min(top_of(child)[1] for child in children) - drop
        child_centers = [top_of(child)[0] for child in children]
        parts = [
            f'<line class="compact-family" x1="{px}" y1="{py}" x2="{px}" y2="{line_y}" />',
            f'<line class="compact-family" x1="{min(child_centers)}" y1="{line_y}" x2="{max(child_centers)}" y2="{line_y}" />',
        ]
        for child in children:
            cx, cy = top_of(child)
            parts.append(f'<line class="compact-family" x1="{cx}" y1="{line_y}" x2="{cx}" y2="{cy}" />')
        return "\n".join(parts)

    def couple_children(a: str, b: str, children: list[str], drop: int = 30) -> str:
        center_x = (normal_center(a)[0] + normal_center(b)[0]) / 2
        center_y = normal_center(a)[1]
        line_y = min(top_of(child)[1] for child in children) - drop
        child_centers = [top_of(child)[0] for child in children]
        parts = [
            f'<line class="compact-family" x1="{center_x}" y1="{center_y}" x2="{center_x}" y2="{line_y}" />',
            f'<line class="compact-family" x1="{min(child_centers)}" y1="{line_y}" x2="{max(child_centers)}" y2="{line_y}" />',
        ]
        for child in children:
            cx, cy = top_of(child)
            parts.append(f'<line class="compact-family" x1="{cx}" y1="{line_y}" x2="{cx}" y2="{cy}" />')
        return "\n".join(parts)

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title2 desc2">',
        '  <title id="title2">Lebanese Arabic family tree screenshot style layout</title>',
        '  <desc id="desc2">A compact one-tree SVG variant for lesson 12, styled after the user-provided screenshot, generated from local CSV and plain-text exports.</desc>',
        "  <style>",
        "    .compact-bg { fill: #4b8879; }",
        "    .compact-family { stroke: #c9bbc0; stroke-width: 5; fill: none; stroke-linecap: round; }",
        "    .compact-couple { stroke: #d7c7b5; stroke-width: 3; fill: none; stroke-linecap: round; }",
        "    .compact-card rect { stroke: #8d746a; stroke-width: 2; rx: 10; ry: 10; }",
        "    .compact-card.female rect { fill: #ff6a6c; }",
        "    .compact-card.male rect, .compact-card.neutral rect { fill: #fffdf9; }",
        "    .compact-translit { font-family: Arial, sans-serif; font-size: 12px; font-weight: 700; fill: #171312; }",
        "    .compact-translit.featured { font-size: 13px; }",
        "    .compact-arabic { font-family: 'Noto Naskh Arabic', 'Amiri', serif; font-size: 15px; fill: #171312; }",
        "    .compact-arabic.featured { font-size: 16px; }",
        "    .avatar-shell { fill: #f7ece3; stroke: rgba(0,0,0,0.15); stroke-width: 1.5; }",
        "    .avatar-core { fill: #6b8d7e; }",
        "    .avatar-text { font-family: Arial, sans-serif; font-size: 24px; font-weight: 700; fill: #fffaf5; }",
        "  </style>",
        f'  <rect class="compact-bg" x="0" y="0" width="{width}" height="{height}" />',
        sibling_bus("LXPV4", "N7KUB", ["Q2R2G", "R69PZ", "VQYK9"], 42),
        sibling_bus("DD56C", "NECA6", ["IW8LA", "KOHKZ", "UTEGJ"], 42),
        couple_line_compact("Q2R2G", "SZKMD"),
        couple_line_compact("R69PZ", "OTMR8"),
        couple_line_compact("VQYK9", "IW8LA"),
        couple_line_compact("KOHKZ", "G6AQX"),
        couple_line_compact("UTEGJ", "ZWNPD"),
        sibling_bus("VQYK9", "IW8LA", ["EPTAW", "START", "MDG4X"], 32),
        couple_line_compact("HFYF5", "EPTAW"),
        couple_line_compact("START", "M6OLG"),
        couple_line_compact("MDG4X", "UW810"),
        couple_children("Q2R2G", "SZKMD", ["CBUPO", "EXAY8"], 32),
        couple_children("R69PZ", "OTMR8", ["V07RX", "GD8CH"], 32),
        couple_children("HFYF5", "EPTAW", ["SW73F", "YO9NZ"], 32),
        couple_children("START", "M6OLG", ["POXJI", "TAV32"], 32),
        couple_children("MDG4X", "UW810", ["SY510", "MC8ND"], 32),
        couple_children("KOHKZ", "G6AQX", ["OER1D", "OR4CF"], 32),
        couple_children("UTEGJ", "ZWNPD", ["G4T20", "X06TU"], 32),
    ]

    for person_id, (x, y, featured) in positions.items():
        lines.append(compact_card_svg(people[person_id], x, y, featured=featured))

    lines.append("</svg>")
    return "\n".join(lines)


def photo_data_uri(person_id: str) -> str | None:
    if not PHOTOS_DIR.exists():
        return None
    for ext, mime in (("png", "image/png"), ("jpg", "image/jpeg"), ("jpeg", "image/jpeg"), ("webp", "image/webp")):
        candidate = PHOTOS_DIR / f"{person_id}.{ext}"
        if candidate.exists():
            encoded = base64.b64encode(candidate.read_bytes()).decode("ascii")
            return f"data:{mime};base64,{encoded}"
    return None


def main() -> None:
    SVG_PATH.write_text(build_svg(), encoding="utf-8")
    SCREENSHOT_STYLE_SVG_PATH.write_text(build_screenshot_style_svg(), encoding="utf-8")
    print(f"Wrote {SVG_PATH}")
    print(f"Wrote {SCREENSHOT_STYLE_SVG_PATH}")


if __name__ == "__main__":
    main()
