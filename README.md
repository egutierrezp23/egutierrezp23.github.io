# egutierrezp23.github.io

Sitio personal y portafolio profesional de Emmanuel Gutierrez Pizarro,
Director de JP Asesores S.R.L. Bilingue (ingles por defecto, espanol con boton).

Construido con Astro y desplegado en GitHub Pages.

## Setup rapido

```bash
npm install
npm run dev      # desarrollo local en http://localhost:4321
npm run build    # compila a /dist
```

## Estructura

```
src/
  layouts/Layout.astro      Nav bilingue + footer + toggles (idioma y tema)
  pages/
    index.astro             Inicio
    proyectos.astro         Proyectos / Work
    publicaciones.astro     Publicaciones / Publications
    trayectoria.astro       Trayectoria / About
    contacto.astro          Contacto / Contact
  styles/global.css         Estilos + sistema bilingue + tema claro/oscuro
public/
  img/                      Foto de perfil (profile.jpg)
  files/                    PDFs (censo, balance fiscal, CV)
  favicon.svg
.github/workflows/deploy.yml   Deploy automatico a GitHub Pages
```

## Tipografia

Titulos en Fraunces, cuerpo en Hanken Grotesk (Google Fonts, cargadas en global.css).

## Bilingue (ingles por defecto)

Cada pagina tiene dos bloques: `<div class="lang-en">` y `<div class="lang-es">`.
El boton de idioma en la navegacion muestra el bloque activo y guarda la
preferencia. El sitio arranca en ingles.

Para editar un texto, busque la frase en su idioma dentro del bloque
correspondiente y cambiela. Para agregar contenido nuevo, agreguelo en AMBOS
bloques.

## Articulos en espanol mostrados en ingles

En la pagina de Publicaciones, los articulos originalmente en espanol se
muestran con un resumen en ingles (bloque .lang-en) y un enlace
"Read original (Spanish)" que apunta al medio original. Vea el bloque de
ejemplo en publicaciones.astro y dupliquelo por cada articulo.

## Agregar PDFs

Suba los archivos a public/files/ con nombres sin espacios ni tildes
(ej: balance-fiscal-nosara.pdf). Quedan en
https://TU-USUARIO.github.io/files/balance-fiscal-nosara.pdf

## Foto de perfil

Coloque profile.jpg en public/img/ y en index.astro (en AMBOS bloques de
idioma) reemplace `<span class="avatar-initials">EG</span>` por
`<img src="/img/profile.jpg" alt="Emmanuel Gutierrez Pizarro">`.

## Tema claro / oscuro

Claro por defecto. El boton de sol/luna activa el oscuro y guarda la preferencia.

## Deploy

Cada push a main dispara el workflow de GitHub Actions que compila y publica.
Activar en: Settings > Pages > Source: GitHub Actions.
