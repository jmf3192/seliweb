# Esquema de contenido y dirección de la web

## Qué aporta cada web

| Web | Papel | Ideas que incorporamos |
| --- | --- | --- |
| [Elena Ventura](https://www.byelenaventura.com/) | Inspiración visual principal | Nombre destacado, navegación breve, imágenes grandes, selección de trabajos y fichas de proyecto. |
| [María Orellana](https://mariaorellana.es/) | Inspiración alternativa | Sensibilidad editorial, espacio entre piezas y una presentación personal directa. |
| [Rosa Copado](https://rosacopado.cargo.site/) | Inspiración alternativa | Portfolio fotográfico sencillo, cuadrícula y contacto accesible. |
| [Araceli: hoteles](https://aracelisansano.my.canva.site/) | Fuente de contenido | Posicionamiento en hoteles, espacios y experiencias; fotografías, talleres, stories y vídeos. |
| [Araceli: portfolio general](https://aracelisansano.my.canva.site/portfolioaracelisansano) | Fuente de contenido | Biografía, servicios, experiencia, clientes, fotografía, vídeo, estrategia y redes sociales. |
| [Araceli: edición de vídeo](https://aracelisansano.my.canva.site/copia-de-portfolio-araceli-sansano) | Fuente de contenido | Muestras de edición y piezas audiovisuales. |

Los recursos visuales de la nueva web proceden únicamente de las tres páginas de Araceli. Las otras webs orientan el diseño.

## Mapa de la primera versión

```text
Selección / Inicio
├── Hoteles & experiencias
├── Hotel Daia
├── Historias en movimiento
├── Talleres & encuentros
├── La Palapa
└── La vida en los detalles

Hoteles → colecciones relacionadas + Vacaciones Desconecta
Fotografía → colecciones fotográficas
Vídeo → Historias en movimiento + La Palapa
Sobre mí / Contacto → biografía, servicios, experiencia y enlaces
```

Cada colección tiene URL propia, texto breve, galería o vídeos y acceso al siguiente trabajo. Las fotografías se amplían en un visor con navegación por teclado; los vídeos se reproducen a petición del visitante.

## Contenido disponible y pendiente

| Sección | Disponible en Canva | Qué falta concretar |
| --- | --- | --- |
| Identidad | Nombre Araceli Sansano; fotógrafa, creativa y creadora de contenido. | Aprobar tipografía, pequeño acento de color y forma de presentar el nombre. |
| Inicio | Fotografías de hoteles, arquitectura, talleres y detalles; vídeos de portfolio. | Confirmar selección, orden y portada de cada colección. |
| Hoteles | Imágenes de espacios y experiencias, contenido social y trabajo para Hotel Daia y Vacaciones Desconecta. | Identificar el alojamiento de las fotografías que no vienen etiquetadas. |
| Fotografía | Fotografías de arquitectura, gastronomía, personas, objetos, actividades y detalles. | Nombres de encargos, clientes, localización y año cuando interese mostrarlos. |
| Vídeo | 28 vídeos publicados entre las tres fuentes. | Título, cliente, papel de Araceli (grabación, edición o ambos), créditos y subtítulos/transcripciones revisados. |
| Sobre mí | Retrato, presentación y experiencia profesional. | Aprobar la versión resumida del texto y el énfasis en hoteles frente a otros sectores. |
| Servicios | Fotografía; vídeo y edición; contenido, estrategia y gestión de redes. | Confirmar servicios vigentes y si se describirán entregables concretos. |
| Contacto | Dos correos, Instagram, TikTok y teléfono en las fuentes. | Elegir correo definitivo y confirmar si se mostrará el teléfono. |
| Publicación | Repositorio GitHub y primera versión estática preparada para Pages. | Dominio propio, idioma adicional y texto legal aplicable a la web definitiva. |

## Criterios aplicados al modelo

- Idioma inicial: español, siguiendo las fuentes.
- Fondo claro, nombre en tipografía condensada, navegación sencilla y grandes fotografías. El acento terracota es una propuesta de diseño.
- «Hoteles & experiencias», «Historias en movimiento», «Talleres & encuentros» y «La vida en los detalles» son agrupaciones editoriales propuestas, no nombres de encargos confirmados.
- Hotel Daia, Vacaciones Desconecta y La Palapa se presentan como trabajos identificados porque sus fuentes los nombran. Las imágenes de Daia y los vídeos de La Palapa se vinculan a las páginas que los identifican.
- No se han asignado años ni resultados comerciales a proyectos sin información verificable.
- El correo del modelo es `aracelisansano@gmail.com`, tomado de la web principal de hoteles. El correo alternativo del portfolio es `araceli.sa@hotmail.com`. El teléfono no se muestra en esta versión hasta decidirlo.
- La biografía y las descripciones están adaptadas para lectura web a partir del contenido existente; necesitan aprobación editorial final.
- El equipo del «media kit» se conserva en el registro de contenido, sin ocupar una página propia por ahora.
- Los vídeos recuperados mantienen el audio de la fuente. La versión definitiva necesita subtítulos o transcripciones revisados para las piezas con voz.

## Recuperación del material

Se han archivado **148 recursos: 119 imágenes, 28 vídeos y 1 animación GIF**, unos 470 MB en total (incluyen fotografías, logos, gráficos y variantes usadas en Canva).

- Imágenes: se selecciona la variante de mayor resolución publicada por identificador, hasta 2400 píxeles en su lado mayor.
- Vídeos: se elige el flujo de mayor resolución publicado y se une a su audio sin recodificar. Las resoluciones dependen de cada pieza; algunas llegan a 1920 × 1080 o 1080 × 1920.
- La calidad recuperada es la máxima accesible desde la web publicada. No equivale necesariamente al archivo de cámara o al original subido al editor de Canva.
- Los archivos de máxima calidad se conservan en `assets/originals/`, con un inventario de procedencia, dimensiones, tamaño y SHA-256 en `docs/media-inventory.json`.
- `docs/source-content.json` conserva los textos y la asociación entre páginas de Canva e identificadores de recursos.
- El sitio sirve copias WebP en varios tamaños y vídeos optimizados; los archivos archivados permanecen intactos.
- Los HTML y datos brutos de Canva quedan fuera de Git y de Pages. Pages publica exclusivamente `site/`.

## Siguiente revisión contigo

1. Aprobar la estructura y decidir el énfasis principal de la web.
2. Ajustar la selección y el orden de fotografías y vídeos.
3. Identificar los proyectos sin nombre y completar créditos.
4. Revisar biografía, servicios, contacto y descripciones.
5. Refinar diseño y preparar dominio/contenido definitivo.
