#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__author__ =      "Andrés Fernández Burón"
__description__ = "Python interactive script to scrape and analyze the response for an URI request"
__date__ =        "14-06-2022"
__copyright__ =   "Copyright 2022-2023, Andrés Fernández Burón"
__license__ =     "AGPL-3.0"
__version__ =     "0.1"
__status__ =      "Production"
__maintainer__ =  "Andrés Fernández Burón"
__email__ =       "https://github.com/AndresFernandezBuron/scrape-uri/issues/new/choose"
"""

from .user import clear_screen
from .user import ask_a_number
from .scrape import strip_whitespaces

# ------------------------------------------------------------------------------
# IMPRIMO EN CONSOLA, LA CABECERA DEL SCRIPT
# ------------------------------------------------------------------------------
def print_header( uri='' ):
    clear_screen()
    print('=========================================')
    print(' Andres Fernandez Buron')
    print(' Junio de 2022')
    print(' Scrapear y analizar la respuesta a una URI')
    #print(' Scrape & analyze the response for a request')
    print('=========================================')
    print()
    if uri != '':
        print(f" REQUEST:  {uri}")


# ------------------------------------------------------------------------------
# IMPRIMO EN CONSOLA, LA INFORMACIÓN DE USO DEL SCRIPT
# ------------------------------------------------------------------------------
def print_script_help():
    print(' Tienes que pasar al script, la URI cómo parámetro.\n')
    print(' Ejemplos de uso:\n')
    print(f"\t python scrape-uri https://paginaweb.com/")
    print(f"\t python scrape-uri https://paginaweb.com")
    print(f"\t python scrape-uri paginaweb.com\n\n")
    exit()

# ------------------------------------------------------------------------------
# IMPRIMO EN CONSOLA, LA INFORMACIÓN DE LA RESPUESTA
# ------------------------------------------------------------------------------
def print_request_info( response ):
    print(f" RESPONSE: {response.url}")
    print()
    print(f" STATUS:       {response.status_code} {response.reason}")
    print(f" CONTENT-TYPE: {response.headers['Content-type']}")
    print(f" ENCODING:     {response.encoding}")

# ------------------------------------------------------------------------------
# IMPRIMO EN CONSOLA, LA INFORMACIÓN DEL DOCUMENTO HTML
# ------------------------------------------------------------------------------
def print_html_info( soup ):
    print('\n-----------------------------------------')
    print('\tHTML DOCUMENT BASIC INFO:')
    print('-----------------------------------------\n')
    if( soup.find('title') ):
        print(f" TITLE:       {soup.title.string}")
    if( soup.find('description') ):
        print(f" DESCRIPTION: {soup.find('meta', attrs={'name':'description'})['content']}")
    if( soup.find('keywords') ):
        print(f" KEYWORDS:    {soup.find('meta', attrs={'name':'keywords'})['content']}")
    if( soup.find('h1') ):
        print(f" H1:          {soup.h1.string}")
    print()
    print(f" SCRIPTS:     {len(soup.find_all('script'))}")
    print(f" STYLES:      {len(soup.find_all('link', attrs={'rel':'stylesheet','type':'text/css'}))}")
    print()
    print(f" ANCHORS:     {len(soup.find_all('a'))-len(soup.find_all('a', attrs={'href':'#'}))-len(soup.find_all('a', attrs={'href':None}))}")
    print(f" FORMS:       {len(soup.find_all('form'))}")
    print()
    print(f" WORDS:       {len(strip_whitespaces(soup.body.get_text()).split(' '))}")
    print(f" LETTERS:     {len(strip_whitespaces(soup.body.get_text()))}")

# ------------------------------------------------------------------------------
# IMPRIMO EN CONSOLA, EL MENÚ PRINCIPAL
# ------------------------------------------------------------------------------
def print_menu( content_type ):
    print('\n-----------------------------------------')
    print(' Opciones:')
    print('-----------------------------------------\n')
    print('  0 -> Ver las cabeceras HTTP')
    if( 'text/' in content_type ):
        print('  1 -> Ver el contenido')
    print()
    print('  2 -> Exportar el contenido')
    if( 'text/html' in content_type ):
        print()
        print('  3 -> Buscar en el DOM, en base a una etiqueta HTML')
        print('  4 -> Buscar en el texto de la página web, un texto (case sensitive)')
        print('  5 -> Buscar en el documento, un texto (case insensitive)')
    print('\n -1 -> Salir\n')

# ------------------------------------------------------------------------------
# DEVUELVO INT CON LA OPCIÓN INTRODUCIDA POR EL USUARIO
# ------------------------------------------------------------------------------
def get_op_menu(  content_type  ):
    while True:
        op = ask_a_number('Selecciona una opción')
        if( type(op) == int ):
            if( op == -1):
                break
            elif 'text/html' in content_type:
                if( op>=0 and op<=5 ):
                    break
            elif 'text/' in content_type:
                if( op>=0 and op<=2 ):
                    break
            else:
                if( op==0 or op==2 ):
                    break
    return op

# ------------------------------------------------------------------------------
# MUESTRO EN LA CONSOLA LAS CABECERAS HTTP
# ------------------------------------------------------------------------------
def print_http_headers( response ):
    print('\n-----------------------------------------')
    print('\tHTTP HEADERS:')
    print('-----------------------------------------\n')
    for name in response.headers:
        value = str(response.headers[name])
        sep = ''
        if ',' in value:
            sep = ','
        elif ';' in value:
            sep = ';'
        print('-----------------------------------------')
        if sep == '':
            print(f" {name.upper()}: {response.headers[name]}")
        else:
            print(f" {name.upper()}:")
            for item in value.split(sep):
                print(f"    {item}")

# ------------------------------------------------------------------------------
# MUESTRO EN LA CONSOLA EL CONTENIDO DE LA RESPUESTA
# ------------------------------------------------------------------------------
def show(response, soup):
    print('\n-----------------------------------------')
    if( 'text/html' in response.headers['Content-type'] ):
        print( soup.prettify() )
    else:
        print( response.text )
    