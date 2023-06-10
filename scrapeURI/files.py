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

import os
from io import BytesIO

# ------------------------------------------------------------------------------
# CREO EL DIRECTORIO, SI NO EXISTE
# ------------------------------------------------------------------------------
def create_dir_if_not_exists( dir_path ):
    if( not os.path.isdir( dir_path ) ):
        try:
            os.makedirs(dir_path, exist_ok=True)
        except Exception as e:
            print(f"\n Error al crear el directorio !!\n {dir_path}\n\n {e}\n")
            exit()

# ------------------------------------------------------------------------------
# EXPORTO TEXTO PLANO A UN FICHERO
# ------------------------------------------------------------------------------
def export_to_text_file( output_file_path, content, charset ):
    create_dir_if_not_exists( os.path.dirname(output_file_path) )
    try:
        with open(output_file_path, 'w', encoding=charset) as file:
            file.write(content)
            file.close()
    except Exception as e:
        print(f"\n Error al exportar el fichero de texto !!\n {output_file_path}\n\n {e}\n")
        exit()

# ------------------------------------------------------------------------------
# EXPORTO CONTENIDO BINARIO A UN FICHERO
# ------------------------------------------------------------------------------
def export_to_binary_file( output_file_path, content ):
    create_dir_if_not_exists( os.path.dirname(output_file_path) )
    try:
        data = BytesIO( content )
        with open(output_file_path, 'wb') as file:
            file.write( data.getbuffer() )
            file.close()
    except Exception as e:
        print(f"\n Error al exportar el fichero binario !!\n {output_file_path}\n\n {e}\n")
        exit()

"""
# ------------------------------------------------------------------------------
# DEVUELVO EL CONTENIDO DE UN FICHERO DE TEXTO
# ------------------------------------------------------------------------------
def get_text_file( file_path ):
    content = None
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            file.close()
    except Exception as e:
        print(f"\n Error al leer el fichero de texto !!\n {file_path}\n\n {e}\n")
        exit()
    return content
"""

# ------------------------------------------------------------------------------
# DEVUELVO LA RUTA NORMALIZADA, EN FUNCIÓN DEL EL SEPARADOR DE RUTAS DEL SISTEMA
# ------------------------------------------------------------------------------
def normalize_path( dir_path ):
    dir_path = dir_path.strip(' ')
    if(os.name=='nt' or os.name=='ce' or os.name=='dos'):
        if( dir_path.find('/') != -1 ):
            dir_path = dir_path.replace('/', os.path.sep)
    elif (os.name=='posix' or os.name=='mac' or os.name=='java'):
        if( dir_path.find('\\') != -1 ):
            dir_path = dir_path.replace('\\', os.path.sep)
    return dir_path
    