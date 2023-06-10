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

from scrapeURI import *

# MUESTRO LA CABECERA
menu.print_header()

# OBTENGO LA URI PASADA CÓMO PARAMETRO O TERMINO
import sys
if( len(sys.argv) == 2 ):
    URI = sys.argv[1]
    if( URI.endswith('-h') or URI.endswith('-help') ):
        menu.print_script_help()
    URI = scrape.normalize_URI( URI )
else:
    print(' No se ha recibido ningún parámetro.\n')
    menu.print_script_help()

# REALIZO LA PETICIÓN
print(f" REQUEST:  {URI}")
response = scrape.scrap_URI(URI)

# SI HAY RESPUESTA MUESTRO LA INFO, SI NO, TERMINO
if response != None:
    menu.print_request_info( response )

# SI LA RESPUESTA ES 200 LA PROCESO, SI NO, TERMINO
if( response.ok ):

    # SI LA RESPUESTA ES TEXTO PLANO, INTENTO INSTANCIAR BEAUTIFULSOUP
    soup = None
    if( 'text/' in response.headers['Content-type'] ):
        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(response.text, features='lxml')
        except Exception as e:
            soup = None

    # SI LA RESPUESTA ES HTML
    if( 'text/html' in response.headers['Content-type'] ):    
        menu.print_html_info( soup )

    # MENÚ PRINCIPAL
    print('\n-----------------------------------------\n')
    if( user.ask_a_bool('Quieres analizar el contenido ?') ):

        op = 0
        while op != -1:

            menu.print_header( response.url )
            menu.print_request_info( response )
            menu.print_menu( response.headers['Content-type'] )
            op = menu.get_op_menu( response.headers['Content-type'] )
            
            if op != -1:
                menu.print_header( response.url )
                functions.handle_menu_op( op, response, soup )
                user.ask_continue()

print()
print('----------------------------------------')
print(' FIN DE SCRIPT\n')