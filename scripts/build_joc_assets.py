#!/usr/bin/env python3
"""Rebuild JoC showcase images from genuine, author-supplied cropped screenshots.

Requires Pillow. Crops live in art/joc-screenshots/; do not replace them
with mock data. Command: python scripts/build_joc_assets.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "art" / "joc-screenshots"
OUT = ROOT / "assets"
BG = "#0B140F"
PANEL = "#10251A"
EDGE = "#29503B"
GREEN = "#7BD998"
LIME = "#B9ED93"
INK = "#E9F1E9"
SOFT = "#AFC3B2"
FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONTR = "/usr/share/fonts/opentype/inter/Inter-Regular.otf"
FONTM = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

def font(size, kind="regular"):
    for path in ({"regular": [FONTR, "C:/Windows/Fonts/arial.ttf"],
                  "bold": [FONTB, "C:/Windows/Fonts/arialbd.ttf"],
                  "mono": [FONTM, "C:/Windows/Fonts/consola.ttf"]}[kind]):
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            pass
    return ImageFont.load_default()

def wrap(d, text, x, y, max_width, size=19, step=28):
    words = text.split()
    current = ""
    for word in words:
        trial = (current + " " + word).strip()
        if current and d.textbbox((0, 0), trial, font=font(size))[2] > max_width:
            d.text((x, y), current, font=font(size), fill=SOFT)
            y += step
            current = word
        else:
            current = trial
    if current:
        d.text((x, y), current, font=font(size), fill=SOFT)

def main():
    archive = Image.open(SOURCE / "archive-crop.png").convert("RGB")
    weekly = Image.open(SOURCE / "weekly-crop.png").convert("RGB")
    athlete = Image.open(SOURCE / "athlete-crop.png").convert("RGB")
    card = Image.new("RGB", (1200, 580), BG)
    d = ImageDraw.Draw(card)
    d.rounded_rectangle((2, 2, 1197, 577), radius=22, outline=EDGE, width=2)
    for x in range(0, 1200, 46):
        d.line((x, 0, x, 580), fill="#102219")
    for y in range(0, 580, 46):
        d.line((0, y, 1200, y), fill="#102219")
    d.rounded_rectangle((36, 31, 342, 66), radius=9, fill="#193426", outline="#315D43")
    d.text((52, 40), "FEATURED COMMUNITY PROJECT", font=font(14, "mono"), fill=LIME)
    d.text((34, 95), "JESTEM", font=font(61, "bold"), fill=INK)
    d.text((34, 166), "OD CZESIA", font=font(61, "bold"), fill=GREEN)
    d.text((36, 256), "The club remembers.", font=font(28, "bold"), fill=INK)
    wrap(d, "A historical home for our Strava club leaderboards, progress, PBs and race memories.", 37, 305, 482)
    for i, text in enumerate(["WEEK-BY-WEEK HISTORY", "PERSONALIZED ATHLETE PROFILES", "BADGES, PBs & RACE RESULTS"]):
        y = 408 + i * 33
        d.rounded_rectangle((37, y + 3, 52, y + 18), radius=3, fill="#325A3D")
        d.text((63, y), text, font=font(14, "mono"), fill=LIME)
    d.text((38, 537), "stats.odczesia.run  ↗", font=font(18, "mono"), fill=GREEN)
    d.rounded_rectangle((574, 65, 1171, 524), radius=13, fill="#111D15", outline="#4D765A", width=2)
    scaled = archive.resize((569, round(archive.height * 569 / archive.width)), Image.Resampling.LANCZOS)
    card.paste(scaled.crop((0, 0, 569, 410)), (588, 101))
    d.text((594, 78), "REAL PRODUCT / WEEKLY ARCHIVE", font=font(13, "mono"), fill=SOFT)
    d.rectangle((588, 501, 1157, 511), fill="#193B29")
    card.save(OUT / "joc-archive.png", optimize=True)

    gallery = Image.new("RGB", (1200, 550), BG)
    gd = ImageDraw.Draw(gallery)
    gd.text((24, 19), "INSIDE THE CLUB ARCHIVE", font=font(23, "bold"), fill=INK)
    gd.text((25, 50), "Real interface screenshots • historic weeks, club podiums and individual profiles", font=font(15), fill=SOFT)
    for i, (label, source) in enumerate([
        ("01  WEEKLY STANDINGS", weekly),
        ("02  HISTORICAL WEEKS", archive),
        ("03  ATHLETE PROFILES", athlete),
    ]):
        x, y, width, height = 24 + i * 395, 99, 371, 415
        gd.rounded_rectangle((x, y, x + width, y + height), radius=12, fill=PANEL, outline=EDGE, width=2)
        gd.text((x + 17, y + 15), label, font=font(13, "mono"), fill=LIME)
        sw, sh = width - 28, height - 70
        shot = source.copy()
        shot.thumbnail((sw, sh), Image.Resampling.LANCZOS)
        gd.rectangle((x + 14, y + 46, x + 14 + sw, y + 46 + sh), fill="#F3F0E7")
        gallery.paste(shot, (x + 14 + (sw - shot.width) // 2, y + 46 + (sh - shot.height) // 2))
        gd.text((x + 16, y + height - 19), "stats.odczesia.run", font=font(11, "mono"), fill=SOFT)
    gallery.save(OUT / "joc-gallery.png", optimize=True)
    print("Updated JoC images from real screenshots")

if __name__ == "__main__":
    main()
