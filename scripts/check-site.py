"""Check local HTML navigation, media and basic document structure before deployment."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re

ROOT = Path(__file__).resolve().parents[1] / 'site'
errors = []

class Page(HTMLParser):
    def __init__(self, file):
        super().__init__()
        self.file = file
        self.headings = 0
        self.refs = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'h1': self.headings += 1
        if tag == 'img' and not a.get('alt') and 'lightbox-image' not in a.get('class', ''):
            errors.append(f'{self.file}: image without alt')
        if tag == 'video' and ('controls' not in a or a.get('preload') != 'none'):
            errors.append(f'{self.file}: video without controls or lazy loading')
        for key in ['src', 'href', 'poster']:
            if a.get(key): self.refs.append(a[key])
        if a.get('srcset'):
            self.refs.extend(x.strip().split()[0] for x in a['srcset'].split(','))

pages = list(ROOT.rglob('*.html'))
references = 0
for file in pages:
    parsed = Page(file)
    parsed.feed(file.read_text())
    if parsed.headings != 1: errors.append(f'{file}: expected one h1, found {parsed.headings}')
    for ref in parsed.refs:
        url = urlsplit(ref)
        if url.scheme or url.netloc or not url.path: continue
        path = unquote(url.path)
        target = ROOT / path.removeprefix('/seliweb/') if path.startswith('/seliweb/') else file.parent / path
        if not target.exists(): errors.append(f'{file}: missing {ref}')
        references += 1
for file in ROOT.rglob('*.css'):
    for ref in re.findall(r"url\(['\"]?([^)'\"]+)", file.read_text()):
        if not (file.parent / ref).is_file(): errors.append(f'{file}: missing {ref}')
for file in ROOT.rglob('*'):
    if file.is_file() and file.stat().st_size == 0 and file.name != '.nojekyll': errors.append(f'Empty file: {file}')
if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print(f'PASS: {len(pages)} HTML pages, {references} local references, media attributes and CSS assets')
