#!/usr/bin/env python3
"""Read-only HTTP checks against the *published* Yangdeok website.

Run in an internet-connected environment: python scripts/check_live_seo.py
Exit 0 only when all 7 pages and SEO files pass.
"""
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from html.parser import HTMLParser
from xml.etree import ElementTree as ET
import sys, re
BASE='https://yangdukparents.github.io'
PAGES=['','garden.html','reading.html','culture.html','explore.html','experience-2026.html','school-life-2026.html']
URLS=[BASE+'/' + n for n in PAGES]
class MetaParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.canon=[]; self.og={}; self.names={}
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if tag=='link' and attrs.get('rel')=='canonical':self.canon.append(attrs.get('href'))
        if tag=='meta' and attrs.get('property','').startswith('og:'):
            self.og[attrs['property']]=attrs.get('content')
        if tag=='meta' and attrs.get('name') in ('description','robots','google-site-verification','naver-site-verification'):
            self.names[attrs['name']]=attrs.get('content')
def get(url):
    try:
        with urlopen(Request(url,headers={'User-Agent':'YangdeokSEOAudit/1.0','Cache-Control':'no-cache'}),timeout=15) as resp:
            return resp.status,resp.headers.get('Content-Type',''),resp.read()
    except (HTTPError,URLError,TimeoutError) as exc:
        return None,'',str(exc).encode()
ok=True
for url in URLS:
    code,typ,data=get(url)
    v=MetaParser()
    if code==200:
        v.feed(data.decode('utf-8','replace'))
    good=code==200 and v.canon==[url] and v.og.get('og:url')==url and bool(v.og.get('og:image'))
    print(('PASS' if good else 'FAIL'),code,url,'canonical:',v.canon,'OG:',bool(v.og))
    ok &= good
sitemap_url=BASE+'/sitemap.xml'
code,typ,data=get(sitemap_url)
urls=[]
try:
    root=ET.fromstring(data)
    urls=[n.text for n in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
except ET.ParseError:pass
good=code==200 and urls==URLS
print(('PASS' if good else 'FAIL'),code,sitemap_url,'URLs:',len(urls),'Content-Type:',typ)
ok &= good
code,typ,data=get(BASE+'/robots.txt')
good=code==200 and ('Sitemap: '+sitemap_url).encode() in data
print(('PASS' if good else 'FAIL'),code,BASE+'/robots.txt')
ok &= good
code,typ,data=get(BASE+'/assets/yangdeok-social-preview.jpg')
good=code==200 and typ.lower().startswith('image/')
print(('PASS' if good else 'FAIL'),code,'Social image','Content-Type:',typ)
ok &= good
print('RESULT:', 'PASS' if ok else 'FAIL (check above)')
sys.exit(0 if ok else 1)
