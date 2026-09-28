# Web de Araceli Sansano

Primera versión del portfolio: 13 páginas estáticas, 7 colecciones, 35 imágenes seleccionadas y 8 vídeos. Diseño adaptable a móvil, galerías ampliables y vídeos con controles.

- [Esquema de contenidos y decisiones pendientes](docs/CONTENT-PLAN.md)
- [Inventario de los 148 recursos recuperados](docs/media-inventory.json)
- [Textos y asociación de recursos de las fuentes](docs/source-content.json)
- [Contenido editable de la web](content.json)
- [Descarga de los recursos en máxima calidad publicada (470 MB)](https://github.com/jmf3192/seliweb/releases/tag/recursos-canva-2026-09-28)

## Objetivo

Crear una web de portfolio visual para Araceli Sansano. La información de partida procede de sus webs actuales en Canva; [Elena Ventura](https://www.byelenaventura.com/) es la inspiración visual principal, con [María Orellana](https://mariaorellana.es/) y [Rosa Copado](https://rosacopado.cargo.site/) como referencias alternativas.

## Fuentes de contenido actuales

- [Web sobre fotografía para hoteles](https://aracelisansano.my.canva.site/): presenta a Araceli como fotógrafa y creadora de contenido para hoteles y alojamientos. Destaca fotografía de espacios y experiencias, contenido para redes sociales, stories, vídeos, talleres y eventos.
- [Portfolio general](https://aracelisansano.my.canva.site/portfolioaracelisansano): reúne presentación personal, experiencia, vídeos, fotografía, marcas, equipo, habilidades y contacto. Se describe como creativa y creadora de contenido; también trabaja en estrategia y gestión de redes sociales.
- [Portfolio de edición de vídeo](https://aracelisansano.my.canva.site/copia-de-portfolio-araceli-sansano): muestra una selección visual de vídeos editados por Araceli.

Estas páginas son la fuente inicial para seleccionar y adaptar textos, proyectos y material visual. No se asume que toda su estructura deba trasladarse a la nueva web.

## Información identificada

- **Nombre:** Araceli Sansano.
- **Ámbitos de trabajo:** fotografía, vídeo, creación de contenido, edición y gestión de redes sociales; especial interés en hoteles, alojamientos y experiencias.
- **Experiencia mencionada:** Hotel Daia, Vacaciones Desconecta, club La Palapa y ECUE, entre otros trabajos recogidos en el portfolio general.
- **Redes:** Instagram `@aracelisansano`; el portfolio general también enlaza a TikTok con el mismo usuario.
- **Contacto:** la web de hoteles muestra `aracelisansano@gmail.com` y un teléfono; el portfolio general muestra `araceli.sa@hotmail.com`. Hay que decidir qué datos publicar en la nueva web.

## Referencias de diseño

- **Elena Ventura (principal):** portada centrada en imágenes grandes de proyectos, composición limpia sobre fondo claro, nombre destacado y navegación por trabajos, categorías y contacto.
- **María Orellana:** composición editorial más libre, con imágenes de distintos tamaños y bastante espacio entre ellas; navegación mínima para explorar proyectos y acceder a la información personal.
- **Rosa Copado:** cuadrícula fotográfica, cabecera discreta y acceso directo a trabajos, contacto e Instagram.

Tomaremos estas ideas como orientación visual, sin copiar contenido, imágenes ni diseño de forma literal.

## Propuesta inicial de la web

1. **Inicio / proyectos destacados:** una selección de trabajos con fotografías o vídeos de gran tamaño. Cada pieza llevará a su ficha.
2. **Ficha de proyecto:** título, imágenes o vídeo y, cuando proceda, una breve descripción, cliente, año y créditos.
3. **Sobre mí / contacto:** presentación breve, correo y enlaces profesionales o sociales.
4. **Navegación:** selección, hoteles, fotografía, vídeo y contacto.

## Dirección visual y experiencia

- Estilo editorial y sobrio: fondo claro, tipografía con personalidad y protagonismo de las imágenes.
- Composición adaptable a móvil y escritorio; las imágenes conservarán sus proporciones y el texto seguirá siendo legible.
- Interacciones sencillas para recorrer los proyectos, con especial atención a la rapidez de carga y la accesibilidad básica.

## Material y decisiones pendientes

- Selección y orden de proyectos; fotografías, vídeos, textos, créditos y permisos de uso de los materiales actuales.
- Categorías, si hacen falta, y páginas adicionales.
- Correo y teléfono que se publicarán, idioma o idiomas y dominio definitivo.
- Preferencias concretas de tipografía, color y composición dentro de las referencias.

## Desarrollo y publicación

El sitio está en `site/`. GitHub Actions publica exclusivamente esa carpeta en Pages al subir cambios a `main`.

**Estado de Pages:** pendiente de activación. GitHub devuelve que el plan actual no admite Pages para este repositorio privado. Hace falta autorizar el cambio de visibilidad a público o disponer de un plan compatible; el primer flujo de despliegue no se ha completado por este motivo.

```sh
# Vista previa (no requiere instalar dependencias)
python3 -m http.server 4173 --directory site

# Regenerar las páginas después de editar content.json o el generador
python3 scripts/build-site.py

# Comprobar referencias locales y estructura
python3 scripts/check-site.py
node --check site/assets/main.js
```

Para volver a recuperar y preparar los recursos se necesitan Python, Pillow y FFmpeg:

```sh
python3 scripts/collect-media.py
python3 scripts/prepare-site-media.py
python3 scripts/build-site.py
```

Los archivos de máxima calidad se conservan en `assets/originals/` y en la descarga adjunta a la release `recursos-canva-2026-09-28`. Se excluyen del historial Git junto con los datos brutos de Canva; el inventario permite localizar y verificar cada archivo. Las fuentes tipográficas Barlow Condensed y DM Sans se sirven localmente y sus licencias están incluidas.

## Validación del modelo

- Comprobadas 13 páginas HTML y 416 referencias locales, incluidos imágenes, vídeos y tipografías.
- Revisado el diseño en escritorio y en anchuras móviles de 390 y 320 píxeles.
- Verificado el visor de fotografías: apertura, siguiente imagen, cierre con Escape y devolución del foco.
- Verificada la reproducción de vídeo y la carga diferida del resto de las piezas.

## Estado editorial

El modelo está preparado para revisión. La selección, las agrupaciones editoriales, los textos y el correo de contacto son decisiones iniciales que se detallan en el esquema de contenidos. Faltan títulos y créditos de algunas piezas y subtítulos o transcripciones revisados para vídeos con voz.
