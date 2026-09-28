"""Generate web copies; maximum-quality files in assets/originals remain untouched."""
import concurrent.futures
import json
import io
import pathlib
import subprocess
from PIL import Image, ImageOps

ROOT = pathlib.Path(__file__).resolve().parents[1]
content = json.loads((ROOT / 'content.json').read_text())
inventory = {x['id']: x for x in json.loads((ROOT / 'docs/media-inventory.json').read_text())}
image_ids = {content['portrait']}
video_ids = set()
for project in content['projects']:
    image_ids.update(project['images'])
    video_ids.update(project['videos'])
out = ROOT / 'site/assets'
(out / 'images').mkdir(parents=True, exist_ok=True)
(out / 'video').mkdir(parents=True, exist_ok=True)

for key in sorted(image_ids):
    original = ImageOps.exif_transpose(Image.open(ROOT / inventory[key]['path'])).convert('RGB')
    for width in [640, 1280, 1920]:
        image = original.copy()
        image.thumbnail((width, width * 3))
        image.save(out / 'images' / f'{key}-{width}.webp', quality=88, method=6)

def video(key):
    original = ROOT / inventory[key]['path']
    poster = out / 'images' / f'{key}-poster.webp'
    target = out / 'video' / f'{key}.mp4'
    if not poster.exists():
        result = subprocess.run(['ffmpeg', '-v', 'error', '-ss', '2', '-i', str(original), '-frames:v', '1',
                        '-vf', 'scale=1200:1200:force_original_aspect_ratio=decrease', '-f', 'image2pipe', '-c:v', 'png', '-'], check=True, capture_output=True)
        Image.open(io.BytesIO(result.stdout)).convert('RGB').save(poster, quality=88, method=6)
    if not target.exists():
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(original),
                        '-vf', "scale='min(1080,iw)':-2", '-c:v', 'libx264', '-preset', 'fast', '-crf', '23',
                        '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', str(target)], check=True)
    return key

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    for key in pool.map(video, sorted(video_ids)):
        print('Prepared', key, flush=True)
print(f'{len(image_ids)} images; {len(video_ids)} videos ready for the site')
