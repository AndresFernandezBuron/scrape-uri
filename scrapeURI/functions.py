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

import re

from .user import *
from .files import *
from .menu import *

from .scrape import strip_whitespaces

# FILES OUTPUT PATH
output_path = 'data/output/'
output_path = f"{os.path.dirname(os.path.dirname(__file__))}{os.path.sep}{output_path}"

# ------------------------------------------------------------------------------
# EXPORTO EL CONTENIDO DE LA RESPUESTA A FICHERO
# ------------------------------------------------------------------------------
def export(output_path, response, soup):
    path = get_filepath_for_URI(output_path, response.url)
    print(f"\n Exportando a fichero...\n\n {os.path.dirname(path)}")
    if( 'text/html' in response.headers['Content-type'] ):
        if( not path.endswith('.html') ):
            path = f"{path}.html"
        export_to_text_file(path, soup.prettify(), response.encoding)
    elif( 'text/' in response.headers['Content-type'] ):
        export_to_text_file(path, response.text, response.encoding)
    else:
        export_to_binary_file(path, response.content )
    print(f"\n {os.path.basename(path)}")

# ------------------------------------------------------------------------------
# BUSCO UNA ETIQUETA EN EL CÓDIGO HTML
# ------------------------------------------------------------------------------
def search_html_tag( soup ):
    print('\n BUSCO UNA ETIQUETA EN EL CÓDIGO HTML')
    tagname = ask_a_value('\nIntroduce el nombre de la etiqueta HTML', 'Ejemplo: div\n\n Buscar: ')
    founded = soup.find_all( tagname.lower() )
    if( len(founded) > 0 ):
        print(f"\n Encontrados: {len(founded)}\n")
        if( ask_a_bool('Quieres listarlos ?') ):
            print()
            for tag in founded:
                print(f"-----------------------------------------\n{strip_whitespaces(tag)}")
    else:
        print(f"\n No se ha encontrado ninguna etiqueta {tagname}\n")
        
# ------------------------------------------------------------------------------
# BUSCO UN TEXTO EN EL LA PÁGINA WEB
# ------------------------------------------------------------------------------
def search_text_in_webpage( soup ):
    print('\n BUSCO UN TEXTO EN EL LA PÁGINA WEB')
    searched = ask_a_value('\nIntroduce el texto que quieres buscar en la página web', 'Ejemplo: precio\n\n Buscar: ')
    plain_text = soup.body.get_text()
    if( searched in plain_text ):    
        founded = soup.find_all('', string=re.compile(searched))
        if( len(founded) > 0 ):
            print(f"\n Encontrados: {len(founded)}\n")
            if( ask_a_bool('Quieres listarlos ?') ):
                print()
                for tag in founded:
                    print(f"-----------------------------------------\n{strip_whitespaces(tag.parent)}")
        else:
            print(f"\n No se ha encontrado el texto: {searched}\n")
    else:
        print(f"\n No se ha encontrado el texto: {searched}\n")
    
# ------------------------------------------------------------------------------
# BUSCO UN TEXTO EN EL CÓDIGO HTML
# ------------------------------------------------------------------------------
def search_text_in_html( soup ):
    print('\n BUSCO UN TEXTO EN EL CÓDIGO HTML')
    searched = ask_a_value('\nIntroduce el texto que quieres buscar en el código HTML', 'Ejemplo: id="nav"\n\n Buscar: ')
    searched = searched.lower()
    founded = []
    all = soup.select('*')
    for tag in all:
        if( searched in str(tag).lower() ):
            ok = True
            for t in tag.children:
                if( searched in str(t).lower() ):
                    ok = False
                    break
            if( ok and tag not in founded ):
                founded.append(tag)
    if( len(founded) > 0 ):
        print(f"\n Encontrados: {len(founded)}\n")
        if( ask_a_bool('Quieres listarlos ?') ):
            print()
            for tag in founded:
                print(f"-----------------------------------------\n{strip_whitespaces(tag)}")
    else:
        print(f"\n No se ha encontrado el texto: {searched}\n")

# ------------------------------------------------------------------------------
# DEVUELVO LA RUTA RELATIVA PARA EL FICHERO HTML DE OUTPUT
# ------------------------------------------------------------------------------
def get_filepath_for_URI( output_path, URI ):
    filepath = URI.replace('://', '/')
    if( '?' in filepath ):
        filepath = filepath.replace('?', '/')
    if( ':' in filepath ):
        filepath = filepath.replace(':', '-')
    if( filepath[len(filepath)-1:] == '/' ):
        filepath = filepath[:len(filepath)-1]
    if( filepath.count('/') < 2 ):
        parts = filepath.split('/')
        name = parts[len(parts)-1]
        filepath = f"{filepath}/{name}"
    return normalize_path(f"{output_path}{filepath}")
    
# ------------------------------------------------------------------------------
# GESTIONO LA OPCIÓN INTRODUCIDA POR EL USUARIO EN EL MENÚ
# ------------------------------------------------------------------------------
def handle_menu_op( op, response, soup ):
    # OP 0 - VER LAS CABECERAS HTTP
    if( op == 0 ):
        print_http_headers(response)
    # OP 1 - VER CONTENIDO
    elif( op==1 and 'text/' in response.headers['Content-type'] ):
        show(response, soup)
    # OP 2 - EXPORTAR CONTENIDO
    elif( op == 2 ):
        export(output_path, response, soup)
    # OPS 3, 4 y 5
    elif( 'text/html' in response.headers['Content-type'] ):
        # OP 3 - BUSCAR TAG HTML
        if( op == 3 ):
            search_html_tag( soup )
        # OP 4 - BUSCAR TEXTO
        elif( op == 4 ):
            search_text_in_webpage( soup )
        # OP 5 - BUSCAR TEXTO EN CODIGO
        elif( op == 5 ):
            search_text_in_html( soup )
    # OP -1 - TERMINAR
    elif( op == -1 ):
        print('\n TERMINANDO')
