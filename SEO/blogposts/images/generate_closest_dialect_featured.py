from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "closest-dialect-to-msa-featured.png"
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
    return ImageFont.truetype(str(Path(r"C:\Windows\Fonts") / name), size=size)


TITLE_FONT = load_font("georgiab.ttf", 64)
SUBTITLE_FONT = load_font("segoeui.ttf", 25)
LABEL_FONT = load_font("arialbd.ttf", 24)
SMALL_FONT = load_font("arialbd.ttf", 20)
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


def draw_pill(draw: ImageDraw.ImageDraw, xy, text, fill, text_fill, pad_x=18, pad_y=10, radius=24):
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

    # Subtle background texture.
    texture = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    tex_draw = ImageDraw.Draw(texture)
    for step in range(0, WIDTH + HEIGHT, 20):
        tex_draw.line((step, 0, step - 220, HEIGHT), fill=(255, 255, 255, 18), width=2)
    texture = texture.filter(ImageFilter.GaussianBlur(1))
    img.alpha_composite(texture)

    # Right-side arcs, aligned with the existing blogpost image language.
    draw_arc_band(draw, (830, -80, 1310, 400), 210, 355, ACCENT_RED, 16)
    draw_arc_band(draw, (900, 0, 1340, 440), 210, 355, ACCENT_GOLD, 10)
    draw_arc_band(draw, (960, 70, 1370, 480), 210, 355, ACCENT_CREAM, 8)

    # Left card.
    card_box = (78, 90, 862, 546)
    make_shadow(img, card_box, radius=28)
    rounded_box(draw, card_box, radius=28, fill=CARD)

    # Small label.
    draw.text((116, 118), "MODERN STANDARD ARABIC", font=LABEL_FONT, fill=TEXT_LIGHT)
    draw.rounded_rectangle((116, 146, 252, 154), radius=4, fill=ACCENT_GOLD)

    # Main title.
    title = "Closest Dialect\nTo MSA?"
    draw.multiline_text((116, 194), title, font=TITLE_FONT, fill=TEXT_LIGHT, spacing=4)

    # Supporting subtitle.
    subtitle = "It depends what \"closest\" means:\nstructure, vocabulary, or perception."
    draw.multiline_text((118, 360), subtitle, font=SUBTITLE_FONT, fill=TEXT_MUTED, spacing=8)

    # Footer lockup.
    if LOGO.exists():
        logo = Image.open(LOGO).convert("RGBA")
        target_height = 28
        scale = target_height / logo.height
        logo = logo.resize((int(logo.width * scale), target_height), Image.LANCZOS)
        
        logo_x, logo_y = 118, 450
        img.alpha_composite(logo, (logo_x, logo_y))
        
        # Calculate the bottom of the logo
        logo_bottom = logo_y + target_height
        
        # SET YOUR GAP HERE (Distance from logo to the gold line)
        GAP = 12 
        
        line_top = logo_bottom + GAP
        line_bottom = line_top + 6  # 6 is the thickness of the line
        
        # Draw the gold line relative to the logo
        draw.rounded_rectangle((116, line_top, 210, line_bottom), radius=3, fill=ACCENT_GOLD)
        
        # Position the text slightly below the line
        text_y = line_bottom + 8
        draw.text((116, text_y), "lebanese-arabic.com", font=LABEL_FONT, fill=TEXT_LIGHT)
    else:
        # Fallback if no logo exists
        draw.text((116, 500), "lebanese-arabic.com", font=LABEL_FONT, fill=TEXT_LIGHT)

    # 1. DEFINE COORDINATES
    cx, cy = 1000, 202  # Badge center stays the same
    
    # Use a consistent X-coordinate for the left edge
    LEFT_ALIGN_X = 880 
    
    pill_data = [
        {"pos": (LEFT_ALIGN_X, 312), "text": "Structure: Najdi", "fill": CARD, "text_fill": TEXT_LIGHT},
        {"pos": (LEFT_ALIGN_X, 372), "text": "Vocabulary: Levantine", "fill": ACCENT_GOLD, "text_fill": "#2a241d"},
        {"pos": (LEFT_ALIGN_X, 432), "text": "Perception: Levantine & Iraqi", "fill": ACCENT_CREAM, "text_fill": CARD}
    ]

    # 2. DRAW CONNECTORS FIRST
    for data in pill_data:
        px, py = data["pos"]
        # Calculate dynamic height for vertical centering
        bbox = draw.textbbox((0, 0), data["text"], font=SMALL_FONT)
        p_height = (bbox[3] - bbox[1]) + 20 # 20 is pad_y * 2
        
        target_x = px - 10 # Offset the dot slightly to the left of the pill
        target_y = py + (p_height // 2)
        
        # The connector "elbow"
        # 1. Vertical line drops from the MSA badge center (cx)
        draw.line((cx, cy, cx, target_y), fill=data["fill"], width=4)
        # 2. Horizontal line goes from the central axis to the pill's left side
        draw.line((cx, target_y, target_x, target_y), fill=data["fill"], width=4)
        
        # 3. Small joint dot (now perfectly aligned vertically)
        draw.ellipse((target_x - 5, target_y - 5, target_x + 5, target_y + 5), fill=data["fill"])

    # 3. DRAW BADGE AND PILLS LAST
    draw_badge(draw, (cx, cy), 66, "MSA", ACCENT_RED, TEXT_LIGHT)
    for data in pill_data:
        draw_pill(draw, data["pos"], data["text"], data["fill"], data["text_fill"])

    # Small footer note.
    draw.text((791, 585), "Linguistics | Arabic dialects | Lebanese Arabic", font=MICRO_FONT, fill=TEXT_DARK)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    img.convert("RGB").save(OUTPUT, quality=95)
    print(OUTPUT)


if __name__ == "__main__":
    generate()
