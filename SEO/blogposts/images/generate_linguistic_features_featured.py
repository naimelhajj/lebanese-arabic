from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "linguistic-features-featured.png"
LOGO = Path(__file__).resolve().parents[2] / "pages" / "lesson12" / "cropped-hiba-logo-without-najem-white.png"

WIDTH = 1200
HEIGHT = 630

BG = "#efe4d3"
CARD = "#123f38"
ACCENT_RED = "#c43b2e"
ACCENT_GOLD = "#e4ab41"
ACCENT_CREAM = "#f6ecd9"
TEXT_LIGHT = "#f7efe2"
TEXT_MUTED = "#d8ddd8"
TEXT_DARK = "#6a736f"


def load_font(name: str, size: int) -> ImageFont.FreeTypeFont:
    try:
        return ImageFont.truetype(str(Path(r"C:\Windows\Fonts") / name), size=size)
    except Exception:
        return ImageFont.load_default()


TITLE_FONT = load_font("georgiab.ttf", 58)
SUBTITLE_FONT = load_font("segoeui.ttf", 26)
LABEL_FONT = load_font("arialbd.ttf", 24)
SMALL_FONT = load_font("arialbd.ttf", 18)
BADGE_FONT = load_font("arialbd.ttf", 26)
MICRO_FONT = load_font("segoeui.ttf", 17)


def rounded_box(draw: ImageDraw.ImageDraw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def draw_arc_band(draw: ImageDraw.ImageDraw, box, start, end, color, width):
    draw.arc(box, start=start, end=end, fill=color, width=width)


def make_shadow(base: Image.Image, box, radius=28, offset=(10, 18), alpha=120):
    shadow = Image.new("RGBA", base.size, (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    x1, y1, x2, y2 = box
    ox, oy = offset
    shadow_draw.rounded_rectangle((x1 + ox, y1 + oy, x2 + ox, y2 + oy), radius=radius, fill=(0, 0, 0, alpha))
    shadow = shadow.filter(ImageFilter.GaussianBlur(24))
    base.alpha_composite(shadow)


def draw_badge(draw: ImageDraw.ImageDraw, center, radius, text, fill, text_fill):
    x, y = center
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=fill)
    bbox = draw.textbbox((0, 0), text, font=BADGE_FONT)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((x - tw / 2, y - th / 2 - 2), text, font=BADGE_FONT, fill=text_fill)


def draw_pill(draw: ImageDraw.ImageDraw, xy, text, fill, text_fill, pad_x=15, pad_y=8, radius=22):
    tx, ty = xy
    bbox = draw.textbbox((0, 0), text, font=SMALL_FONT)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    box = (tx, ty, tx + tw + pad_x * 2, ty + th + pad_y * 2)
    draw.rounded_rectangle(box, radius=radius, fill=fill)
    draw.text((tx + pad_x, ty + pad_y - 1), text, font=SMALL_FONT, fill=text_fill)
    return box


def generate():
    img = Image.new("RGBA", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)

    texture = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    tex_draw = ImageDraw.Draw(texture)
    for step in range(0, WIDTH + HEIGHT, 20):
        tex_draw.line((step, 0, step - 220, HEIGHT), fill=(255, 255, 255, 18), width=2)
    texture = texture.filter(ImageFilter.GaussianBlur(1))
    img.alpha_composite(texture)

    # Right-side decorative arcs: slightly smaller and shifted right.
    draw_arc_band(draw, (870, -70, 1300, 360), 210, 355, ACCENT_RED, 14)
    draw_arc_band(draw, (930, 0, 1320, 400), 210, 355, ACCENT_GOLD, 9)
    draw_arc_band(draw, (980, 60, 1340, 430), 210, 355, ACCENT_CREAM, 7)

    card_box = (78, 90, 862, 546)
    make_shadow(img, card_box, radius=28)
    rounded_box(draw, card_box, radius=28, fill=CARD)

    draw.text((116, 118), "LEBANESE ARABIC", font=LABEL_FONT, fill=TEXT_LIGHT)
    draw.rounded_rectangle((116, 146, 252, 154), radius=4, fill=ACCENT_GOLD)

    title = "Linguistic\nFeatures"
    draw.multiline_text((116, 190), title, font=TITLE_FONT, fill=TEXT_LIGHT, spacing=4)

    subtitle = "Phonology, grammar, diglossia,\nand code-switching in Lebanon."
    draw.multiline_text((118, 350), subtitle, font=SUBTITLE_FONT, fill=TEXT_MUTED, spacing=8)

    if LOGO.exists():
        logo = Image.open(LOGO).convert("RGBA")
        target_height = 28
        scale = target_height / logo.height
        logo = logo.resize((int(logo.width * scale), target_height), Image.LANCZOS)
        logo_x, logo_y = 118, 450
        img.alpha_composite(logo, (logo_x, logo_y))
        logo_bottom = logo_y + target_height
        gap = 12
        line_top = logo_bottom + gap
        line_bottom = line_top + 6
        draw.rounded_rectangle((116, line_top, 220, line_bottom), radius=3, fill=ACCENT_GOLD)
        draw.text((116, line_bottom + 8), "lebanese-arabic.com", font=LABEL_FONT, fill=TEXT_LIGHT)
    else:
        draw.text((116, 500), "lebanese-arabic.com", font=LABEL_FONT, fill=TEXT_LIGHT)

    cx, cy = 1020, 198
    left_align_x = 890
    pill_data = [
        {"pos": (left_align_x, 300), "text": "Urban + Rural Continuum", "fill": CARD, "text_fill": TEXT_LIGHT},
        {"pos": (left_align_x, 362), "text": "MSA Relationship (Diglossia)", "fill": ACCENT_GOLD, "text_fill": "#2a241d"},
        {"pos": (left_align_x, 424), "text": "French/English Code-Switching", "fill": ACCENT_CREAM, "text_fill": CARD},
    ]

    for data in pill_data:
        px, py = data["pos"]
        bbox = draw.textbbox((0, 0), data["text"], font=SMALL_FONT)
        p_height = (bbox[3] - bbox[1]) + 20
        target_x = px - 10
        target_y = py + (p_height // 2)
        draw.line((cx, cy, cx, target_y), fill=data["fill"], width=4)
        draw.line((cx, target_y, target_x, target_y), fill=data["fill"], width=4)
        draw.ellipse((target_x - 5, target_y - 5, target_x + 5, target_y + 5), fill=data["fill"])

    draw_badge(draw, (cx, cy), 66, "LA", ACCENT_RED, TEXT_LIGHT)
    for data in pill_data:
        draw_pill(draw, data["pos"], data["text"], data["fill"], data["text_fill"])

    draw.text((758, 585), "Lebanese Arabic with Hiba | Linguistics explainer", font=MICRO_FONT, fill=TEXT_DARK)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    img.convert("RGB").save(OUTPUT, quality=95)
    print(OUTPUT)


if __name__ == "__main__":
    generate()
