#!/usr/bin/env python3
"""Generate the Botanical Telemetry README artwork. Pillow only; no remote assets.

Run: pip install Pillow && python scripts/build_assets.py
Edit profile.json to change milestones. Demo chart uses synthetic data only.
"""
from __future__ import annotations
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path
import json, math, random, statistics

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets'
OUT.mkdir(exist_ok=True)
CFG = json.loads((ROOT / 'profile.json').read_text(encoding='utf-8'))
W = 1200
C = {'bg':'#0B100D','surface':'#101B13','panel':'#15241A','panel2':'#1B3022',
     'deep':'#09100B','green':'#58C27D','light':'#B7ED87','white':'#F0F7EF',
     'muted':'#9AADA0','dim':'#617766','line':'#2C4633','black':'#07130C','warm':'#D9DFCF'}
FONT_DIRS=[Path('/usr/share/fonts/opentype/inter'),Path('/usr/share/fonts/truetype/dejavu')]
FONTS = {'bold':['Inter-Bold.otf','DejaVuSans-Bold.ttf'], 'heavy':['Inter-ExtraBold.otf','DejaVuSans-Bold.ttf'],
         'medium':['Inter-Medium.otf','DejaVuSans.ttf'], 'regular':['Inter-Regular.otf','DejaVuSans.ttf'],
         'mono':['DejaVuSansMono.ttf','Inter-Regular.otf']}
def font(sz=20,style='regular'):
    for n in FONTS[style]:
        for d in FONT_DIRS:
            p=d/n
            if p.exists():return ImageFont.truetype(str(p),sz)
    return ImageFont.load_default()
def rgb(hex): return tuple(int(hex[i:i+2],16) for i in (1,3,5))
def base(h):
    im=Image.new('RGB',(W,h),rgb(C['bg']))
    d=ImageDraw.Draw(im)
    for x in range(0,W,52):d.line([(x,0),(x,h)],fill='#102016',width=1)
    for y in range(0,h,52):d.line([(0,y),(W,y)],fill='#102016',width=1)
    d.rounded_rectangle((1,1,W-2,h-2),radius=24,outline=C['line'],width=2)
    return im,d
def txt(d,pos,s,sz=20,color='white',weight='regular',anchor=None):
    d.text(pos,s,font=font(sz,weight),fill=C.get(color,color),anchor=anchor)
def pill(d,x,y,label,fill=None,fg='green',pad=13):
    f=font(16,'mono'); width=int(d.textlength(label,font=f))+2*pad
    d.rounded_rectangle((x,y,x+width,y+33),radius=8,fill=fill or C['panel'],outline=C['line'])
    d.text((x+pad,y+7),label,font=f,fill=C.get(fg,fg))
    return width

def grid_lines(d,x1,y1,x2,y2,step=49):
    for y in range(y1,y2+1,step): d.line((x1,y,x2,y),fill='#284031',width=1)
    for x in range(x1,x2+1,step): d.line((x,y1,x,y2),fill='#17291C',width=1)
def cactus(d,cx,cy,scale=1,foot=0,outlined=False):
    """Geometric original cactus mascot. Anchor cx/cy at its central body."""
    def b(v): return int(v*scale)
    left=cx-b(14); top=cy-b(31); right=cx+b(14); bottom=cy+b(31)
    color=C['green']; lime=C['light']
    d.rounded_rectangle((left,top,right,bottom),radius=b(12),fill=color,outline=lime if outlined else color,width=2)
    d.line([(left,cy+b(8)),(cx-b(30),cy+b(8)),(cx-b(32),cy-b(7))], fill=color,width=b(8),joint='curve')
    d.line([(right,cy),(cx+b(30),cy),(cx+b(31),cy-b(17))],fill=color,width=b(8),joint='curve')
    d.ellipse((cx-b(7),cy-b(13),cx-b(3),cy-b(9)),fill=C['deep'])
    d.ellipse((cx+b(4),cy-b(13),cx+b(8),cy-b(9)),fill=C['deep'])
    d.arc((cx-b(6),cy-b(8),cx+b(7),cy+b(3)),0,180,fill=C['deep'],width=max(1,b(2)))
    d.line([(cx-b(5),bottom),(cx-b(13),bottom+b(11)+foot)],fill=lime,width=b(5))
    d.line([(cx+b(5),bottom),(cx+b(15),bottom+b(11)-foot)],fill=lime,width=b(5))
    d.ellipse((cx-b(2),top-b(6),cx+b(2),top-b(2)),fill=lime)
def topbar(d,label,right='BOTANICAL TELEMETRY / V2.0'):
    d.ellipse((35,29,45,39),fill=C['light'])
    txt(d,(60,26),label,19,'green','mono')
    r=font(15,'mono'); x=W-36-int(d.textlength(right,font=r))
    txt(d,(x,30),right,15,'muted','mono')

def hero_frame(t=0.):
    h=410; im,d=base(h);topbar(d,'PROFILE // DAWIDTHECACTUS')
    d.line((36,69,W-36,69),fill=C['line'],width=2)
    txt(d,(54,98),'DAWID',77,'white','heavy')
    txt(d,(54,177),'THE CACTUS',72,'green','heavy')
    txt(d,(58,270),CFG['headline'],26,'white','medium')
    txt(d,(58,316),'POWER BI   /   SQL   /   PYTHON   /   CURIOUS SIDE PROJECTS',17,'muted','mono')
    # panel backdrop
    d.rounded_rectangle((762,99,1146,350),radius=20,fill=C['surface'],outline=C['line'],width=2)
    txt(d,(782,116),'PACE SIGNAL / LIVE LOOP',16,'green','mono')
    for y in (183,238,293):d.line((786,y,1120,y),fill=C['line'],width=1)
    # animation points move across the time series
    coords=[]
    for i in range(170):
        x=786+i*2
        v=(math.sin(i/13)+.45*math.sin(i/5)+.25*math.sin(i/29))
        y=int(245-43*v)
        coords.append((x,y))
    d.line(coords,fill='#294E36',width=8,joint='curve')
    N=max(8,int(t*(len(coords)-1)))
    d.line(coords[:N],fill=C['green'],width=5,joint='curve')
    # bright moving dot
    px,py=coords[N-1]
    d.ellipse((px-7,py-7,px+7,py+7),fill=C['light'])
    cactus(d,1070,170,0.8,foot=int(3*math.sin(t*math.pi*8)))
    txt(d,(795,314),'SIGNAL FOUND.',17,'light','mono')
    return im

def save_gif(name,frames,duration=85):
    frames[0].save(OUT/name,save_all=True,append_images=frames[1:],duration=duration,loop=0,
                   optimize=True,disposal=2)

def identity():
    h=314; im,d=base(h);topbar(d,'01 / THE PERSON BEHIND THE DATA')
    d.rounded_rectangle((30,75,571,283),radius=18,fill=C['panel'],outline=C['line'],width=2)
    d.rounded_rectangle((591,75,1170,283),radius=18,fill=C['surface'],outline=C['line'],width=2)
    txt(d,(54,101),'MON–FRI  /  PROFESSIONALLY',17,'green','mono')
    txt(d,(54,140),'DATA ANALYST',38,'white','heavy')
    txt(d,(54,195),'Power BI · DAX · SQL · Power Query',22,'white','medium')
    txt(d,(54,239),'Metrics that explain what actually matters.',17,'muted')
    txt(d,(616,101),'AFTER HOURS  /  BY CURIOSITY',17,'light','mono')
    txt(d,(616,140),'CODE FOR FUN',38,'white','heavy')
    txt(d,(616,195),'Python · TypeScript · React · AI tools',22,'white','medium')
    txt(d,(616,239),'Some ideas are too interesting not to build.',17,'muted')
    im.save(OUT/'identity.png',optimize=True)

def milestone_frame(t=1.0):
    h=350;im,d=base(h);topbar(d,'02 / RUNNING TELEMETRY  //  NOT A DEMO')
    txt(d,(45,91),str(CFG['half_marathons_completed']),111,'green','heavy')
    txt(d,(205,112),'HALF MARATHONS',38,'white','heavy')
    txt(d,(205,157),'COMPLETED',38,'white','heavy')
    txt(d,(49,256),'ONE FINISH LINE AT A TIME',17,'muted','mono')
    # mini stats right
    d.rounded_rectangle((802,91,1145,238),radius=17,fill=C['panel'],outline=C['line'],width=2)
    txt(d,(828,113),'NEXT BIG MISSION',17,'muted','mono')
    txt(d,(828,145),CFG['half_marathon_goal'],46,'light','heavy')
    txt(d,(828,204),'HALF MARATHON TARGET',16,'muted','mono')
    d.line((40,281,W-45,281),fill=C['line'],width=2)
    markers=min(CFG['half_marathons_completed'],11)
    # 11 green markers, slight wave pulse
    width=93
    for n in range(11):
        x=58+n*width
        bright=(n+1)<=markers
        color=C['light'] if n==int(t*11)%11 else (C['green'] if bright else C['line'])
        d.rounded_rectangle((x,303,x+72,319),radius=8,fill=color if bright else C['panel'])
        txt(d,(x+35,328),f'{n+1:02}',14,'muted','mono',anchor='mm')
    return im

def tformat(minutes):
    sec=int(round(minutes*60));return f'{sec//3600}:{(sec%3600)//60:02}:{sec%60:02}'

def analytic():
    rng=random.Random(422)
    vals=[max(75,min(195,rng.gauss(113,18))) for _ in range(600)]
    vals.sort();median=statistics.median(vals)
    p90=vals[int(.9*(len(vals)-1))]
    bins=list(range(75,196,5))
    counts=[sum(bins[i]<=v<bins[i+1] for v in vals) for i in range(len(bins)-1)]
    peak=max(range(len(counts)),key=lambda k:counts[k]);highest=counts[peak]
    h=560;im,d=base(h);topbar(d,'03 / ANALYTICS PLAYGROUND')
    txt(d,(40,85),'Half-marathon finish time distribution',35,'white','heavy')
    pill(d,40,138,'SYNTHETIC DATA  /  N = 600')
    pill(d,410,138,'PERFORMANCE DISTRIBUTION',fg='light')
    # columns and scales
    x0=72;ybot=446;H=214;barw=23;gap=9
    d.rounded_rectangle((34,195,878,518),radius=15,fill=C['surface'],outline=C['line'])
    for yi in range(4):
        yy=ybot-int(H*yi/3)
        d.line((66,yy,851,yy),fill=C['line'],width=1)
        txt(d,(48,yy-10),str(int(highest*yi/3)),14,'muted','mono',anchor='ra')
    for i,c in enumerate(counts):
        x=x0+i*(barw+gap)
        hh=int(H*c/highest)
        col=C['light'] if i==peak else (C['green'] if i in range(max(0,peak-3),min(24,peak+4)) else '#355A40')
        d.rounded_rectangle((x,ybot-hh,x+barw,ybot),radius=5,fill=col)
    for i in (0,6,12,18,23):
        txt(d,(x0+i*(barw+gap)+barw//2,470),tformat(bins[i]),13,'muted','mono',anchor='mm')
    txt(d,(70,495),'TIME (H:MM:SS)   /   5-MINUTE BINS',14,'muted','mono')
    # stats panel
    d.rounded_rectangle((902,195,1165,344),radius=14,fill=C['panel'],outline=C['line'])
    txt(d,(925,218),'MEDIAN FINISH',16,'muted','mono')
    txt(d,(925,247),tformat(median),38,'green','heavy')
    d.rounded_rectangle((902,362,1165,518),radius=14,fill=C['panel'],outline=C['line'])
    txt(d,(925,387),'P90 FINISH',16,'muted','mono')
    txt(d,(925,414),tformat(p90),38,'light','heavy')
    txt(d,(925,476),'90% FINISH BY THIS',14,'muted','mono')
    im.save(OUT/'analytics-demo.png',optimize=True)
    (ROOT/'docs'/'synthetic-data.json').write_text(json.dumps({'description':'Random seeded synthetic half-marathon finishing times, no real people or races.',
             'seed':422,'n':600,'median':tformat(median),'p90':tformat(p90),'five_minute_bins':list(zip(bins[:-1],counts))},indent=2),encoding='utf-8')

def projects():
    h=380;im,d=base(h);topbar(d,'04 / THINGS I BUILD FOR FUN')
    cards=[('RunStats Polska','Race results / performance analytics','DATA PRODUCTS',C['green']),
           ('Signature Lab','Vector signatures / motion systems','CREATIVE CODING',C['light']),
           ('InvoicePilot AI','Document intelligence / automation','AI EXPERIMENTS',C['green']),
           ('fballers-lab','Game mechanics / training simulation','SYSTEMS LAB',C['light'])]
    for i,(name,desc,tag,col) in enumerate(cards):
        x=32+(i%2)*573; y=81+(i//2)*139
        d.rounded_rectangle((x,y,x+550,y+126),radius=17,fill=C['panel'] if i%2==0 else C['surface'],outline=C['line'],width=2)
        txt(d,(x+22,y+19),f'0{i+1} / {tag}',16,col,'mono')
        txt(d,(x+22,y+48),name,31,'white','bold')
        txt(d,(x+22,y+91),desc,18,'muted')
        d.ellipse((x+502,y+25,x+517,y+40),fill=col)
    im.save(OUT/'projects.png',optimize=True)

def easter():
    h=176;im,d=base(h);topbar(d,'05 / THE OFFICE  //  EASTER EGG')
    txt(d,(42,77),'BEARS. BEETS. BUSINESS INTELLIGENCE.',35,'white','heavy')
    txt(d,(43,133),'Assistant to the Regional Analyst.   [GIF SLOT RESERVED]',18,'light','mono')
    # cartoon paperclip graph icon, not copyrighted character
    d.ellipse((1088,72,1150,134),outline=C['green'],width=5)
    d.line((1099,125,1134,88),fill=C['light'],width=5)
    im.save(OUT/'office-easter-egg.png',optimize=True)

def preview():
    parts=[OUT/'hero.png',OUT/'identity.png',OUT/'milestones.png',OUT/'analytics-demo.png',OUT/'projects.png',OUT/'office-easter-egg.png']
    gap=18; imgs=[Image.open(p).convert('RGB') for p in parts]
    hh=sum(im.height for im in imgs)+gap*(len(imgs)+1)
    result=Image.new('RGB',(W,hh),rgb(C['bg'])); y=gap
    for im in imgs: result.paste(im,(0,y)); y+=im.height+gap
    result.save(OUT/'preview-full.png',optimize=True)

def main():
    hero=hero_frame(1);hero.save(OUT/'hero.png',optimize=True)
    save_gif('hero.gif',[hero_frame((i+1)/30) for i in range(30)],duration=100)
    m=milestone_frame(1);m.save(OUT/'milestones.png',optimize=True)
    save_gif('milestones.gif',[milestone_frame(i/22) for i in range(22)],duration=130)
    identity();analytic();projects();easter();preview()
    for p in sorted(OUT.glob('*')):print(p.name,round(p.stat().st_size/1024),'KB')
if __name__=='__main__':main()
