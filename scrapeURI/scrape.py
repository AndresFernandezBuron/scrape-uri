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
    
import requests

from .files import *
from .menu import *

# ------------------------------------------------------------------------------
# DEVUELVO LA URI NORMALIZADA
# ------------------------------------------------------------------------------
def normalize_URI( URI ):
    URI = URI.strip(' ')
    if( not URI.startswith('http') ):
        URI = f"http://{URI}"
    if( not URI.endswith('/') ):
        URI = f"{URI}/"
    return URI

# ------------------------------------------------------------------------------
# HAGO UNA PETICIÓN A UNA URI Y DEVUELVO EL CONTENIDO DE LA RESPUESTA O NONE
# ------------------------------------------------------------------------------
def scrap_URI( URI ):
    content = None
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
    try:
        content = requests.get(URI, params={}, headers={'User-Agent': user_agent})
    except Exception as e:
        print(f"\n Error al hacer la petición !!\n\n {e}\n")
        exit()
    return content

# ------------------------------------------------------------------------------
# DEVUELVO EL STR DE UN TAG DE BS4 SIN ESPACIOS BLANCOS GRANDES
# ------------------------------------------------------------------------------
def strip_whitespaces( tag ):
    tag = str( tag )
    tag = tag.strip()
    tag = tag.replace('  ', '')
    tag = tag.replace('\n', '')
    tag = tag.replace('\t', '')
    return tag
