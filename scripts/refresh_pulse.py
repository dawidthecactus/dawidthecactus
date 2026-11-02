#!/usr/bin/env python3
"""Create a self-hosted SVG card using *real* public GitHub API data.

Uses Python stdlib only. Run from GitHub Actions with GH_TOKEN=${{ secrets.GITHUB_TOKEN }}.
If the GitHub API is unavailable, fail without overwriting the existing file.
"""
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from collections import Counter
from xml.sax.saxutils import escape
import json, os

ROOT=Path(__file__).resolve().parents[1]
USERNAME=json.loads((ROOT/'profile.json').read_text(encoding='utf-8'))['username']
OUTPUT=ROOT/'assets'/'github-pulse.svg'
COLORS={'bg':'#0B100D','border':'#2C4633','panel':'#15241A','green':'#58C27D','light':'#B7ED87', 'white':'#F0F7EF','muted':'#9AADA0'}

def svg_text(x,y,content,size=22,color='white',bold=False):
    weight='700' if bold else '400'
    return f'<text x="{x}" y="{y}" font-size="{size}" font-family="Arial, sans-serif" font-weight="{weight}" fill="{COLORS.get(color,color)}">{escape(str(content))}</text>'

def render(public_repos=None,stars=None,active90=None,languages=None,updated=None):
    ready=public_repos is not None
    boxes=[('PUBLIC REPOSITORIES',str(public_repos) if ready else '—'),
           ('STARS RECEIVED',str(stars) if ready else '—'),
           ('ACTIVE IN 90 DAYS',str(active90) if ready else '—')]
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="295" viewBox="0 0 1200 295" role="img" aria-label="Public GitHub repository metrics">',
         f'<rect x="1" y="1" width="1198" height="293" rx="20" fill="{COLORS["bg"]}" stroke="{COLORS["border"]}" stroke-width="2" />',
         svg_text(35,46,'07 / GITHUB PULSE',21,'green',True),
         svg_text(916,46,'BOTANICAL TELEMETRY / LIVE DATA',15,'muted')]
    for i,(title,value) in enumerate(boxes):
        x=34+i*380
        out += [f'<rect x="{x}" y="78" width="364" height="137" rx="15" fill="{COLORS["panel"]}" stroke="{COLORS["border"]}" />',
                svg_text(x+23,117,title,18,'muted'),svg_text(x+23,184,value,56,'green',True)]
    bottom=('TOP LANGUAGES   /   '+', '.join(languages[:4])) if ready and languages else 'WAITING FOR FIRST DATA SYNC'
    footer=('UPDATED UTC: '+updated) if updated else 'RUN THE GITHUB ACTIONS WORKFLOW TO ACTIVATE'
    out += [svg_text(35,252,bottom,19,'light'),svg_text(35,278,footer,13,'muted'),'</svg>']
    OUTPUT.write_text('\n'.join(out),encoding='utf-8')

def fetch_repos():
    token=os.getenv('GH_TOKEN','')
    headers={'Accept':'application/vnd.github+json','User-Agent':'dawidthecactus-profile-card',
             'X-GitHub-Api-Version':'2022-11-28'}
    if token:headers['Authorization']='Bearer '+token
    all_repos=[]
    for page in range(1,31):
        url=f'https://api.github.com/users/{USERNAME}/repos?'+urlencode({'per_page':100,'page':page,'type':'owner'})
        req=Request(url,headers=headers)
        with urlopen(req,timeout=25) as r: data=json.loads(r.read().decode('utf-8'))
        if not isinstance(data,list):raise RuntimeError('GitHub API returned unexpected JSON')
        all_repos.extend(data)
        if len(data)<100:break
    return [r for r in all_repos if not r.get('private',False) and r.get('owner',{}).get('login','').lower()==USERNAME.lower()]

def main():
    repos=fetch_repos()
    cutoff=datetime.now(timezone.utc)-timedelta(days=90)
    active=0
    for repo in repos:
        pushed=repo.get('pushed_at')
        if pushed and datetime.fromisoformat(pushed.replace('Z','+00:00'))>=cutoff: active+=1
    langs=Counter(r['language'] for r in repos if r.get('language'))
    render(public_repos=len(repos),stars=sum(r.get('stargazers_count',0) for r in repos),
           active90=active,languages=[k for k,_ in langs.most_common(4)],
           updated=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M'))
    print(f'Synced {len(repos)} public repositories.')
if __name__=='__main__':main()
