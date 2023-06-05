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
def print_header():
    clear_screen()
    print('=========================================')
    print(' Andrés Fernández Burón')
    print(' Junio de 2022')
    print(' Scrapear y analizar la respuesta a una URI')
    #print(' Scrape & analyze the response for request')
    print('=========================================')
    print()

# ------------------------------------------------------------------------------
# IMPRIMO EN CONSOLA, LA INFORMACIÓN DE USO DEL SCRIPT
# ------------------------------------------------------------------------------
def print_script_help():
    print(' Tienes que pasar al script, la URI cómo parámetro.\n')
    print(' Ejemplos:\n')
    print(f"\t python scrape-uri https://paginaweb.com/\n\n")
    print(f"\t python scrape-uri https://paginaweb.com\n")
    print(f"\t python scrape-uri paginaweb.com\n")
    exit()

# ------------------------------------------------------------------------------
# IMPRIMO EN CONSOLA, LA INFORMACIÓN DE LA RESPUESTA
# ------------------------------------------------------------------------------
def print_request_info( response ):
    print(f" Response:     {response.url}")
    print()
    print(f" Estatus:      {response.status_code} {response.reason}")
    print()
    print(f" Content-Type: {response.headers['Content-type']}")
    print(f" Encoding:     {response.encoding}")

# ------------------------------------------------------------------------------
# IMPRIMO EN CONSOLA, LA INFORMACIÓN DEL DOCUMENTO HTML
# ------------------------------------------------------------------------------
def print_html_info( soup ):
    print('\n-----------------------------------------\n')
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
    print()
    print(' 0 -> Ver las cabeceras HTTP')
    print(' 1 -> Ver el contenido')
    print(' 2 -> Exportar el contenido')
    if( 'text/html' in content_type ):
        print()
        print(' 3 -> Buscar en el DOM, en base a una etiqueta HTML')
        print(' 4 -> Buscar en el texto de la página web, un texto (case sensitive)')
        print(' 5 -> Buscar en el documento, un texto (case insensitive)')
    print('\n -1 -> Salir')
    print()

# ------------------------------------------------------------------------------
# DEVUELVO INT CON LA OPCIÓN INTRODUCIDA POR EL USUARIO
# ------------------------------------------------------------------------------
def get_op_menu():
    num_ops = 5
    while True:
        op = ask_a_number('Selecciona una opción')
        if( type(op) == int ):
            if( op>=-1 and op<=num_ops ):
                break
    return op

# ------------------------------------------------------------------------------
# MUESTRO EN LA CONSOLA LAS CABECERAS HTTP
# ------------------------------------------------------------------------------
def print_http_headers( response ):
    print('\n-----------------------------------------')
    print('\n Cabeceras HTTP:\n')
    for name in response.headers:
        print(f" {name}:\t{response.headers[name]}")
        """
        if( ';' in response.headers[name] ):
            print(f" {name}:")
            for item in response.headers[name].split(';'):
                print(f"\t{item}")
        else:
            print(f" {name}:\t{response.headers[name]}")
        """

# ------------------------------------------------------------------------------
# MUESTRO EN LA CONSOLA EL CONTENIDO DE LA RESPUESTA
# ------------------------------------------------------------------------------
def show(response, soup):
    print('\n-----------------------------------------')
    if( 'text/html' in response.headers['Content-type'] ):
        print( soup.prettify() )
    else:
        print( response.text )
    