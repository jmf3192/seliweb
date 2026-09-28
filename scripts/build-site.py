"""Build a portable, static portfolio. Only site/ is deployed to GitHub Pages."""
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / 'site'
DATA = json.loads((ROOT / 'content.json').read_text())
PROJECTS = DATA['projects']
INVENTORY = {x['id']: x for x in json.loads((ROOT / 'docs/media-inventory.json').read_text())}
ESC = html.escape
NAV = [('index.html', 'Selección'), ('hoteles.html', 'Hoteles'), ('fotografia.html', 'Fotografía'),
       ('video.html', 'Vídeo'), ('contacto.html', 'Contacto')]

def picture(key, alt, prefix='', eager=False, extra=''):
    item = INVENTORY[key]
    return f'''<img class="{extra}" src="{prefix}assets/images/{key}-1280.webp"
      srcset="{prefix}assets/images/{key}-640.webp {min(640,item["width"])}w, {prefix}assets/images/{key}-1280.webp {min(1280,item["width"])}w, {prefix}assets/images/{key}-1920.webp {min(1920,item["width"])}w"
      sizes="(max-width: 700px) 100vw, 50vw" width="{item['width']}" height="{item['height']}"
      alt="{ESC(alt)}" loading="{'eager' if eager else 'lazy'}" {'fetchpriority="high"' if eager else ''} decoding="async">'''

def poster(key, alt, prefix='', eager=False):
    item = INVENTORY[key]
    return f'<img src="{prefix}assets/images/{key}-poster.webp" width="{item["width"]}" height="{item["height"]}" alt="{ESC(alt)}" loading="{"eager" if eager else "lazy"}" decoding="async">'

def shell(title, description, body, active='index.html', prefix='', page_class=''):
    nav = ''.join(f'<a href="{prefix}{url}" ' + ('aria-current="page"' if url == active else '') + f'>{label}</a>' for url, label in NAV)
    return f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{ESC(title)} — Araceli Sansano</title><meta name="description" content="{ESC(description)}">
<meta name="theme-color" content="#faf9f6"><meta property="og:title" content="{ESC(title)} — Araceli Sansano">
<meta property="og:description" content="{ESC(description)}"><meta property="og:type" content="website">
<meta property="og:image" content="https://jmf3192.github.io/seliweb/assets/images/MAGwtpu_GCA-1280.webp">
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="{prefix}assets/fonts/barlow-condensed-800.ttf" as="font" type="font/ttf" crossorigin>
<link rel="stylesheet" href="{prefix}assets/style.css"><script src="{prefix}assets/main.js" defer></script></head>
<body class="{page_class}"><a class="skip" href="#contenido">Saltar al contenido</a>
<header class="header"><a class="wordmark" href="{prefix}index.html" aria-label="Araceli Sansano, inicio">ARACELI SANSANO<span class="brand-dot">.</span></a>
<nav aria-label="Navegación principal">{nav}</nav></header>
<main id="contenido">{body}</main>
<footer class="footer"><div class="footer-top"><div><span class="eyebrow">¿CREAMOS ALGO JUNTOS?</span><a class="contact-cta" href="mailto:{DATA['email']}">Hablemos<span aria-hidden="true">↗</span></a></div>
<div class="footer-links"><a href="mailto:{DATA['email']}">{DATA['email']}</a><a href="{DATA['instagram']}" target="_blank" rel="noopener noreferrer">Instagram ↗</a><a href="{DATA['tiktok']}" target="_blank" rel="noopener noreferrer">TikTok ↗</a></div></div>
<div class="footer-bottom"><span>© Araceli Sansano <span data-year>2026</span></span><span>Fotografía, vídeo & contenido</span><a href="#">Volver arriba ↑</a></div></footer>
<dialog class="lightbox" aria-label="Visor de fotografías"><div class="lightbox-bar"><span class="lightbox-count" aria-live="polite"></span><button class="lightbox-close" type="button" aria-label="Cerrar visor">Cerrar ×</button></div><div class="lightbox-stage"><button class="lightbox-prev" type="button" aria-label="Fotografía anterior">←</button><img class="lightbox-image" alt=""><button class="lightbox-next" type="button" aria-label="Fotografía siguiente">→</button></div><p class="lightbox-caption"></p></dialog>
</body></html>'''

def card(project, index, feature=False):
    if project.get('cover_video'):
        visual = poster(project['cover_video'], project['title']) + '<span class="play-badge" aria-hidden="true">↗ VER VÍDEOS</span>'
    else:
        visual = picture(project['cover'], project['title'], eager=feature)
        if feature:
            visual += picture(project['second_cover'], 'Arquitectura y luz junto a la piscina', eager=True)
    return f'''<article class="project-card {'featured' if feature else ''}"><a class="project-link" href="proyectos/{project['slug']}.html"><div class="project-visual {'paired' if feature else ''}">{visual}</div>
<div class="project-caption"><span class="project-number">{index:02}</span><div><h2>{ESC(project['title'])}</h2><p>{ESC(project['subtitle'])}</p></div><span class="project-arrow" aria-hidden="true">↗</span></div></a></article>'''

selected = [p for p in PROJECTS if p['featured']]
body = '<section aria-labelledby="selection-title"><div class="section-kicker"><h1 id="selection-title">Una mirada natural. Historias que se sienten.</h1><span>TRABAJOS SELECCIONADOS ↓</span></div>'
body += '<div class="project-grid">' + ''.join(card(p, i + 1, i == 0) for i, p in enumerate(selected)) + '</div></section>'
body += f'''<section class="about-preview"><span class="eyebrow">DETRÁS DE LA MIRADA</span><div><h2>Observar. Sentir.<br>Contar una historia.</h2><p>Soy Araceli, fotógrafa y creadora de contenido. Transformo espacios, experiencias e ideas en imágenes que conectan, cuidando cada detalle, desde la luz hasta el ritmo del montaje.</p><a class="text-link" href="contacto.html">Un poco más sobre mí ↗</a></div></section>'''
(OUT / 'index.html').write_text(shell('Fotografía, vídeo & contenido', 'Portfolio de Araceli Sansano. Fotografía y creación de contenido para hoteles, marcas y experiencias.', body))

categories = {
    'hoteles': ('Hoteles & experiencias', 'La luz, los espacios y la sensación de estar allí.'),
    'fotografia': ('Fotografía', 'Una forma de mirar lo cotidiano, los lugares y sus detalles.'),
    'video': ('Historias en movimiento', 'Ideas que toman forma. Grabación, storytelling y edición.'),
}
for category, (title, description) in categories.items():
    projects = [p for p in PROJECTS if category in p['categories']]
    body = f'<section><div class="category-heading"><span class="eyebrow">PORTFOLIO / {category.upper()}</span><h1>{title}</h1><p>{description}</p></div><div class="project-grid">'
    body += ''.join(card(p, i + 1) for i, p in enumerate(projects)) + '</div></section>'
    (OUT / f'{category}.html').write_text(shell(title, description, body, active=f'{category}.html'))

(OUT / 'proyectos').mkdir(exist_ok=True)
for i, project in enumerate(PROJECTS):
    body = f'''<a class="back-link" href="../index.html">← Todos los trabajos</a><section class="project-intro"><div><span class="eyebrow">{ESC(project['subtitle'])}</span><h1>{ESC(project['title'])}</h1></div><p>{ESC(project['description'])}</p></section><div class="gallery">'''
    for j, key in enumerate(project['images']):
        alt = f'{project["title"]} — fotografía {j+1}'
        body += f'<a class="gallery-item" href="../assets/images/{key}-1920.webp" data-lightbox data-caption="{ESC(alt)}" aria-label="Ampliar: {ESC(alt)}">{picture(key, alt, "../", eager=j<2)}<span aria-hidden="true">↗</span></a>'
    body += '</div>'
    if project['videos']:
        body += '<div class="video-grid">'
        for j, key in enumerate(project['videos']):
            item = INVENTORY[key]
            body += f'''<figure class="video-item {'landscape' if item['width'] > item['height'] else ''}"><video controls playsinline preload="none" poster="../assets/images/{key}-poster.webp" width="{item['width']}" height="{item['height']}" aria-label="{ESC(project['title'])}, vídeo {j+1}"><source src="../assets/video/{key}.mp4" type="video/mp4"><a href="../assets/video/{key}.mp4">Abrir vídeo</a></video><figcaption><span>{j+1:02} — {ESC(project['title'])}</span><span>{round(item['duration'])} s</span></figcaption></figure>'''
        body += '</div>'
    next_project = PROJECTS[(i + 1) % len(PROJECTS)]
    body += f'<a class="next-project" href="{next_project["slug"]}.html"><span class="eyebrow">SIGUIENTE TRABAJO</span><span>{ESC(next_project["title"])} ↗</span></a>'
    (OUT / 'proyectos' / f'{project["slug"]}.html').write_text(shell(project['title'], project['description'], body, prefix='../', active='', page_class='project-page'))

body = f'''<section class="about-page"><div class="portrait">{picture(DATA['portrait'], 'Araceli Sansano', eager=True)}</div><div class="about-copy"><span class="eyebrow">FOTÓGRAFA & CREADORA DE CONTENIDO</span><h1>Hola,<br>soy Araceli<span class="brand-dot">.</span></h1><p class="lead">Me gusta observar, contar historias y encontrar algo especial en lo cotidiano.</p><p>Combino la fotografía con la creación de contenido para marcas. Desarrollo ideas, grabo y edito vídeos y creo imágenes que conectan con las personas.</p><p>Trabajo con hoteles y alojamientos para mostrar sus espacios, detalles y experiencias con una mirada estética y natural. También gestiono cuentas, diseño estrategias y acompaño a marcas a encontrar su propio estilo.</p><a class="text-link" href="mailto:{DATA['email']}">Cuéntame tu idea ↗</a></div></section>
<section class="services"><div><span class="eyebrow">CÓMO PUEDO AYUDARTE</span><h2>De la idea<br>a la imagen.</h2></div><div class="service-list"><div><span>01</span><h3>Fotografía</h3><p>Espacios, experiencias, producto y detalles. Imágenes que cuentan una historia.</p></div><div><span>02</span><h3>Vídeo & edición</h3><p>Storytelling, grabación y montaje de contenido para marcas y redes sociales.</p></div><div><span>03</span><h3>Contenido & estrategia</h3><p>Dirección creativa, planificación de contenidos y gestión de redes sociales.</p></div></div></section>
<section class="experience"><span class="eyebrow">HE CREADO CONTENIDO PARA</span><p>Hotel Daia <span>·</span> Vacaciones Desconecta <span>·</span> La Palapa <span>·</span> ECUE</p></section>'''
(OUT / 'contacto.html').write_text(shell('Sobre mí & contacto', 'Conoce a Araceli Sansano, fotógrafa y creadora de contenido. Hablemos de tu próximo proyecto.', body, active='contacto.html'))
(OUT / '404.html').write_text(shell('Página no encontrada', 'Vuelve al portfolio de Araceli Sansano.', '<section class="category-heading"><span class="eyebrow">404</span><h1>Esta página se ha ido<br>a buscar la luz.</h1><a class="text-link" href="/seliweb/">Volver al portfolio ↗</a></section>', prefix='/seliweb/'))
(OUT / '.nojekyll').touch()
print('Built 13 static HTML pages in site/')
