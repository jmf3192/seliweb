"""Archive the highest-resolution variants exposed by the three public Canva pages.

Raw Canva data stays local. The clean inventory contains only media URLs and metadata.
Videos use the highest-resolution DASH stream and original audio, remuxed without loss.
"""
import concurrent.futures
import hashlib
import json
import pathlib
import re
import subprocess
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCES = {
    'hoteles': 'https://aracelisansano.my.canva.site/',
    'portfolio': 'https://aracelisansano.my.canva.site/portfolioaracelisansano/',
    'video': 'https://aracelisansano.my.canva.site/copia-de-portfolio-araceli-sansano/',
}

def download(url, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(request, timeout=90) as response:
            path.write_bytes(response.read())
    return path

def walk(value):
    yield value
    if isinstance(value, dict):
        for item in value.values():
            yield from walk(item)
    elif isinstance(value, list):
        for item in value:
            yield from walk(item)

media = {}
pages = {}
for name, base in SOURCES.items():
    raw = download(base, ROOT / 'source-pages' / f'{name}.html').read_text()
    embedded = re.findall(r"JSON\.parse\('((?:\\.|[^'\\])*)'\)", raw)[1]
    data = json.loads(embedded.replace("\\'", "'").replace('\\\\', '\\'))['page']
    pages[name] = []
    for i, page in enumerate(data['A']['A']):
        nodes = list(walk(page))
        text = [x['A'] for x in nodes if isinstance(x, dict) and x.get('A?') == 'A'
                and isinstance(x.get('A'), str) and '\n' in x['A']]
        ids = list(dict.fromkeys(x for x in nodes if isinstance(x, str) and re.fullmatch(r'[MV]A[\w-]{8,}', x)))
        pages[name].append({'page': i + 1, 'texts': text, 'media_ids': ids})
    for asset in data['I']['B']:
        for f in asset['files']:
            if f.get('urlDenied') or f.get('watermarked') or not f['url'].startswith('_assets/media/'):
                continue
            key = asset['id']
            candidate = {'id': key, 'type': 'image', 'url': base + f['url'],
                         'width': f.get('width', 0), 'height': f.get('height', 0), 'quality': f.get('quality'),
                         'sources': [name]}
            if key in media:
                candidate['sources'] = list(dict.fromkeys(media[key]['sources'] + [name]))
            if key not in media or candidate['width'] * candidate['height'] > media[key]['width'] * media[key]['height']:
                media[key] = candidate
            else:
                media[key]['sources'] = candidate['sources']
    for asset in data['I']['C']:
        key = asset['id']
        if key in media:
            media[key]['sources'] = list(dict.fromkeys(media[key]['sources'] + [name]))
            continue
        variants = asset.get('dashVideoFiles', [])
        best = max(variants, key=lambda v: (v['A'] * v['B'], v.get('x', 0))) if variants else None
        f = max(asset['files'], key=lambda v: v['width'] * v['height'])
        item = {'id': key, 'type': 'video', 'url': base + (best['1'] if best else f['url']),
                'width': best['A'] if best else f['width'], 'height': best['B'] if best else f['height'],
                'sources': [name], 'duration': asset.get('durationSeconds'), 'fallback_url': base + f['url']}
        audio = asset.get('dashAudioFiles', [])
        if best and audio:
            item['audio_url'] = base + max(audio, key=lambda a: a.get('x', 0))['1']
        media[key] = item

def obtain(item):
    extension = '.mp4' if item['type'] == 'video' else pathlib.Path(item['url']).suffix
    relative = 'assets/originals/' + item['id'] + extension
    target = ROOT / relative
    if item['type'] == 'video':
        video = download(item['url'], ROOT / 'assets/.download' / (item['id'] + '.mp4'))
        if video.read_bytes()[:3] == b'GIF':
            relative = 'assets/originals/' + item['id'] + '.gif'
            target = ROOT / relative
            target.write_bytes(video.read_bytes())
            item.update(type='animation', path=relative, bytes=target.stat().st_size,
                        sha256=hashlib.sha256(target.read_bytes()).hexdigest())
            return item
        args = ['ffmpeg', '-v', 'error', '-y', '-i', str(video)]
        if item.get('audio_url'):
            audio = download(item['audio_url'], ROOT / 'assets/.download' / (item['id'] + '.m4a'))
            args += ['-i', str(audio), '-map', '0:v:0', '-map', '1:a:0']
        args += ['-c', 'copy', '-movflags', '+faststart', str(target)]
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            subprocess.run(args, check=True)
    else:
        download(item['url'], target)
    item.update(path=relative, bytes=target.stat().st_size, sha256=hashlib.sha256(target.read_bytes()).hexdigest())
    return item

results = []
errors = []
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    futures = {pool.submit(obtain, item): item for item in media.values()}
    for future in concurrent.futures.as_completed(futures):
        try:
            results.append(future.result())
        except Exception as e:
            errors.append({'id': futures[future]['id'], 'error': str(e)})
        if (len(results) + len(errors)) % 20 == 0:
            print(f'Recovered {len(results)}/{len(media)}; errors: {len(errors)}', flush=True)
(ROOT / 'docs').mkdir(exist_ok=True)
(ROOT / 'docs/media-inventory.json').write_text(json.dumps(sorted(results, key=lambda i:i['id']), ensure_ascii=False, indent=2))
(ROOT / 'docs/source-content.json').write_text(json.dumps(pages, ensure_ascii=False, indent=2))
print(json.dumps({'images': sum(i['type']=='image' for i in results), 'videos': sum(i['type']=='video' for i in results),
                  'bytes': sum(i['bytes'] for i in results), 'errors': errors}, indent=2))
if errors:
    raise SystemExit(1)
