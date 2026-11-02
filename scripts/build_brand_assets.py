#!/usr/bin/env python3
"""Render 2.1 botanical branding from the supplied hero artwork, using Pillow.

The image is an original generated graphic. All profile claims are edited in README/profile.json.
Run: pip install Pillow && python scripts/build_brand_assets.py
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path
import math
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets'
W = 1200
FG = '#E8F3E9'
LIME = '#B9F28A'
GREEN = '#72DC94'
SUB = '#AFCCB7'
MONO='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
# on GitHub Actions or most PCs local font paths won't be available; fallback
FONT_CANDIDATES = {'bold':[BOLD, '/usr/share/fonts/opentype/inter/Inter-Bold.otf', 'C:/Windows/Fonts/arialbd.ttf'],
                   'mono':[MONO, 'C:/Windows/Fonts/consola.ttf']}
def f(size,kind='bold'):
    for path in FONT_CANDIDATES[kind]:
        try:return ImageFont.truetype(path,size)
        except OSError:pass
    return ImageFont.load_default()
def draw_base():
    img=Image.open(ROOT/'art'/'cactus-runner-backdrop.png').convert('RGB').resize((W,400),Image.Resampling.LANCZOS)
    # Darken left panel slightly to ensure small-font legibility on mobile
    overlay=Image.new('RGBA',(W,400),(0,0,0,0)); d=ImageDraw.Draw(overlay)
    for x in range(0,775,2):
        alpha=int(105*(1-x/775)**1.2)
        d.rectangle((x,0,x+2,400), fill=(0,8,4,alpha))
    return Image.alpha_composite(img.convert('RGBA'),overlay)
def make_hero(k):
    image=draw_base();d=ImageDraw.Draw(image)
    d.rounded_rectangle((28,26,282,57),radius=9,fill='#142820',outline='#315D42',width=1)
    d.text((42,32),'ANALYST / RUNNER / NERD',font=f(14,'mono'),fill=LIME)
    d.text((36,94),'DAWID',font=f(80),fill=FG,stroke_width=1,stroke_fill='#092014')
    d.text((36,174),'THE CACTUS',font=f(63),fill=GREEN,stroke_width=1,stroke_fill='#092014')
    d.text((39,254),'Data by profession. Code for fun.',font=f(21,'bold'),fill=FG)
    d.text((39,282),'Running for sanity.',font=f(21,'bold'),fill=FG)
    d.line([(39,326),(655,326)], fill='#38694C',width=2)
    d.text((40,344),'POWER BI + DAX + SQL  /  11 HALF MARATHONS',font=f(15,'mono'),fill=LIME)
    # Heartbeat indicator with only dynamic animation, no fabricated metrics
    pulse=(k%10)<6
    d.ellipse((777,32,789,44),fill=LIME if pulse else '#24553B')
    d.text((718,30),'LIVE',font=f(13,'mono'),fill=SUB)
    return image.convert('RGB')
def archive_card():
    im=Image.new('RGB',(W,320),'#0C1610');d=ImageDraw.Draw(im)
    for x in range(0,W,56):d.line([(x,0),(x,320)],fill='#102116',width=1)
    for y in range(0,320,48):d.line([(0,y),(W,y)],fill='#102116',width=1)
    d.rounded_rectangle((2,2,W-3,317),radius=23,outline='#30513A',width=2)
    d.rounded_rectangle((30,25,370,57),radius=9,fill='#173322',outline='#316A47')
    d.text((45,31),'COMMUNITY  /  SWARZEDZ, POLAND',font=f(14,'mono'),fill=LIME)
    d.text((33,78),'JESTEM OD CZESIA',font=f(50),fill=FG)
    d.text((36,148),'RUNNING CLUB ARCHIVE',font=f(28),fill=GREEN)
    d.text((36,209),'Local miles. Shared stories. One archive.',font=f(20,'bold'),fill=SUB)
    d.text((37,272),'stats.odczesia.run',font=f(21,'mono'),fill=LIME)
    # Abstract race track: 3 curving lanes; no invented numeric data
    for j in range(4):
        pts=[]
        for u in range(110):
            x=720+u*4
            y=210+25*j-45*math.sin((u/109)*math.pi*1.3)
            pts.append((x,int(y)))
        d.line(pts,fill=['#20472B','#2C5A38','#36754A','#5BBD76'][j],width=3)
    for x,y in [(760,202),(882,160),(1018,183),(1136,240)]:
        d.ellipse((x-8,y-8,x+8,y+8),fill=LIME)
    d.rounded_rectangle((890,46,1155,87),radius=12,fill='#173322',outline='#4A9962',width=2)
    d.text((908,54),'OPEN THE ARCHIVE  >',font=f(16,'mono'),fill=FG)
    return im
def build_brand_assets():
    OUT.mkdir(exist_ok=True)
    base=make_hero(0)
    base.save(OUT/'hero.png',optimize=True)
    frames=[make_hero(i) for i in range(12)]
    # palette GIF optimizes for README compatibility; small pulsing status LED
    pframes=[im.quantize(colors=128,method=Image.Quantize.MEDIANCUT) for im in frames]
    pframes[0].save(OUT/'hero.gif',save_all=True,append_images=pframes[1:],duration=200,loop=0,optimize=True,disposal=2)
    archive_card().save(OUT/'joc-archive.png',optimize=True)
    parts=[OUT/'hero.png',OUT/'identity.png',OUT/'milestones.png',OUT/'analytics-demo.png',OUT/'joc-archive.png',OUT/'projects.png',OUT/'office-easter-egg.png']
    pieces=[Image.open(x).convert('RGB') for x in parts if x.exists()]
    gap=18
    preview=Image.new('RGB',(W,sum(p.height for p in pieces)+gap*(len(pieces)+1)),'#0B100D')
    y=gap
    for item in pieces:
        preview.paste(item,(0,y)); y+=item.height+gap
    preview.save(OUT/'preview-full.png',optimize=True)
if __name__=='__main__':build_brand_assets()
