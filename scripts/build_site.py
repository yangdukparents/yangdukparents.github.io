#!/usr/bin/env python3
"""Build a GitHub Pages publishable site from static HTML and actual Pages base URL.

Usage: python3 scripts/build_site.py https://actual-host/repo --output _site
Never guess the public URL. GitHub Actions supplies `configure-pages.outputs.base_url`.
"""
import argparse
import re
import shutil
from pathlib import Path
from urllib.parse import urlsplit, quote
from xml.etree import ElementTree as ET

PAGES = ['index.html', 'garden.html', 'reading.html', 'culture.html', 'explore.html', 'experience-2026.html', 'school-life-2026.html']
ROOT = Path(__file__).resolve().parents[1]


def validate_public_base(url: str) -> str:
    parts = urlsplit(url.strip())
    if parts.scheme not in ('https', 'http') or not parts.netloc:
        raise SystemExit('오류: 정확한 공개 URL을 전달해야 합니다. GitHub Actions에서 자동으로 전달됩니다.')
    if parts.query or parts.fragment or parts.username or parts.password:
        raise SystemExit('오류: URL에는 검색어·해시·사용자 정보가 없어야 합니다.')
    if '..' in parts.path.split('/'):
        raise SystemExit('오류: URL 경로에 .. 을 포함할 수 없습니다.')
    return url.strip().rstrip('/')


def build(base, output):
    base = validate_public_base(base)
    output.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / 'styles.css', output/'styles.css')
    shutil.copy2(ROOT / '.nojekyll', output/'.nojekyll')
    shutil.copytree(ROOT/'assets', output/'assets', dirs_exist_ok=True)
    # User-provided ownership verification files must be published unchanged.
    for pattern in ('google*.html', 'naver*.html'):
        for verification_file in ROOT.glob(pattern):
            shutil.copy2(verification_file, output/verification_file.name)
    for name in PAGES:
        text=(ROOT/name).read_text(encoding='utf-8')
        canonical=base + ('/' if name=='index.html' else '/'+name)
        # Source HTML already has a static canonical for branch publishing.
        # Update instead of inserting another tag when deployed with GitHub Actions.
        if not re.search(r'<head\b',text,re.I) or '</head>' not in text.lower():
            raise ValueError(f'{name}: head missing')
        tag=f'<link rel="canonical" href="{canonical}">'
        pattern=r'<link\s+rel="canonical"\s+href="[^"]*"\s*/?>'
        if re.search(pattern,text,flags=re.I):
            text=re.sub(pattern,lambda _:tag,text,count=1,flags=re.I)
        else:
            text=text.replace('</head>',f'{tag}\n</head>',1)
        # Social share URL fields need to reflect project subpaths too.
        text=re.sub(r'(<meta property="og:url" content=")[^"]*(">)',
                    lambda m:m.group(1)+canonical+m.group(2), text, count=1)
        text=re.sub(r'(<meta property="og:image" content=")[^"]*(">)',
                    lambda m:m.group(1)+base+'/assets/yangdeok-social-preview.jpg'+m.group(2),text,count=1)
        (output/name).write_text(text,encoding='utf-8')
    # Sitemap protocol: absolute URLs, all 7 pages; use root / as homepage canonical.
    ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    root=ET.Element('{http://www.sitemaps.org/schemas/sitemap/0.9}urlset')
    for name in PAGES:
        node=ET.SubElement(root,'{http://www.sitemaps.org/schemas/sitemap/0.9}url')
        loc=ET.SubElement(node,'{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
        loc.text=base+ ('/' if name=='index.html' else '/'+name)
    ET.indent(root,space='  ')
    ET.ElementTree(root).write(output/'sitemap.xml',encoding='utf-8',xml_declaration=True)
    (output/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: '+base+'/sitemap.xml\n',encoding='utf-8')
    print(f'Prepared {len(PAGES)} pages with canonical and sitemap for {base}/')
    print('Sitemap:',output/'sitemap.xml')

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('public_base_url', help='Actual GitHub Pages base URL (provided by configure-pages)')
    parser.add_argument('--output',default='_site')
    args=parser.parse_args()
    build(args.public_base_url,Path(args.output))
