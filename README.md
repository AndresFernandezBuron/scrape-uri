
<h1>scrape-uri</h1>
<br>
<p>Python interactive script to scrape and analyze the response for an URI request</p>
<br>
<div>
<table align="center"><tbody>
<tr>
<td>Author</td>
<td>Andrés Fernández Burón</td>
</tr>
<tr>
<td>License</td>
<td>GNU Affero General Public License (AGPL)</td>
</tr>
<tr>
<td>Copyright</td>
<td>2022-2023 &copy; All rights reserved</td>
</tr>
</tbody></table>
</div>
<div align="right">
<b>Language:</b> <a href="#readme-es">Español</a> | <a href="#readme-en">English</a>
</div>
<div id="readme-es">
<hr>
<br>

## Descripción
Es un script interactivo de <a href="https://www.python.org/doc/" target="_blank">Python 3</a>, para realizar una petición HTTP a una URI y analizar la respuesta.

<br>

Este script te permite:
- Ver las cabeceras HTTP de la respuesta
- Ver el contenido (texto) de la respuesta
- Descargar el contenido de la respuesta

<br>

Si la respuesta es código HTML, también muestra la información básica del documento, y te permite:
- Buscar en el DOM, en base a una etiqueta HTML
- Buscar en el texto de la página web, un texto (case sensitive)
- Buscar en el documento, un texto (case insensitive)

<br>

## Instalación
Este proyecto no necesita instalación, pero tiene <a href="#dependencias">requisitos y dependencias</a>.

<br>

## Uso
Se ejecuta cómo cualquier otro script de Python 3.

Recibe un parámetro obligatorio: la URI a scrapear.

<br>

Ejemplos de uso:
<pre>
    python scrape-uri https://www.paginaweb.com/
    python scrape-uri https://paginaweb.com/
    python scrape-uri https://paginaweb.com
    python scrape-uri paginaweb.com
</pre>

<br>

## Dependencias
Este proyecto requiere tener instalado <a href="https://www.python.org/downloads/" target="_blank">Python 3</a>.

También depende de las siguientes librerías de Python:
- <a href="https://requests.readthedocs.io/en/latest/" target="_blank">requests</a>
- <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="_blank">bs4</a>
- <a href="https://lxml.de/index.html#documentation">lxml</a>

<br>

## Compatibilidad
Este script es multiplataforma.

<div align="center">

| OS      | Soportado  |
|---------|------------|
| Unix    | <center>&#10004;</center> |
| Linux   | <center>&#10004;</center> |
| Windows | <center>&#10004;</center> |
| MAC     | Sin probar |
<br>
</div>
</div>
<br>
<div id="readme-en">
<br>
<hr>
<br>

## Description
Is an interactive Python 3 script, to make a HTTP request to an URI and to analyze the response.

<br>

This script allows you to:
- Display the HTTP headers of the response
- Display the text content of the response
- Download the content of the response

<br>

If the response is HTML code, it also displays basic information about the document, and allows you to:
- Search for a HTML tag on the DOM
- Search for a text on the text of the webpage (case sensitive)
- Search for a text on the document (case insensitive)

<br>

## Installation
This project doesn't need installation, but it has <a href="#dependencies">requirements and dependencies</a>.

<br>

## Usage
It runs like any other Python 3 script.

It expects a single required parameter: the URI to scrape.

<br>

Usage example:
<pre>
    python scrape-uri https://www.webpage.com/
    python scrape-uri https://webpage.com/
    python scrape-uri https://webpage.com
    python scrape-uri webpage.com
</pre>

<br>

## Dependencies
This project required to have intalled <a href="https://www.python.org/downloads/" target="_blank">Python 3</a>.

It also depends on the following Python libraries:
- <a href="https://requests.readthedocs.io/en/latest/" target="_blank">requests</a>
- <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="_blank">bs4</a>
- <a href="https://lxml.de/index.html#documentation">lxml</a>

<br>

## Compatibility
This script is multiplatform.

<div align="center">

| OS      | Compatibility |
|---------|---------------|
| Unix    | <center>&#10004;</center> |
| Linux   | <center>&#10004;</center> |
| Windows | <center>&#10004;</center> |
| MAC     | Not tested |
<br>
</div>

</div>