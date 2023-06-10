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

from sys import exit
import os

# ------------------------------------------------------------------------------
# LIMPIO LA CONSOLA
# ------------------------------------------------------------------------------
def clear_screen():
    if(os.name=='nt' or os.name=='ce' or os.name=='dos'):
        os.system('cls')
    #elif (os.name=='posix' or os.name=='mac' or os.name=='java'):
    else:
        os.system('clear')
    
# ------------------------------------------------------------------------------
# ESPERO A QUE EL USUARIO PULSE ENTER
# ------------------------------------------------------------------------------
def ask_continue( msg='Pulsa ENTER para continuar' ):
    input(f"\n\n {msg}")

# ------------------------------------------------------------------------------
# DEVUELVO UN VALOR PEDIDO AL USUARIO
# ------------------------------------------------------------------------------
def ask_a_value( msg='Introduce un valor', detail='' ):
    if( detail == '' ):
        print(f" {msg}: ", end='')
    else:
        print(f" {msg}\n {detail} ", end='')
    value = None
    while( value==None or value=='' ):
        value = input(' ').lstrip().rstrip().strip()
    return value
    
# ------------------------------------------------------------------------------
# DEVUELVO UN BOLEANO PEDIDO AL USUARIO
# ------------------------------------------------------------------------------
def ask_a_bool( msg='Introduce Si ó No' ):
    print(f" {msg}\n\n s/n y/n 0/1\n ")
    bool = None
    while( True ):
        bool = input(' ').lstrip()
        if( bool[:1] in ['S','s','Y','y','1'] ):
            return True
        elif( bool[:1] in ['N','n','0'] ):
            return False
        
# ------------------------------------------------------------------------------
# DEVUELVO UN NÚMERO PEDIDO AL USUARIO
# ------------------------------------------------------------------------------
def ask_a_number( msg='Introduce un número', detail='' ):
    if( detail == '' ):
        print(f" {msg}: ", end='')
    else:
        print(f" {msg}\n\n {detail}\n ")
    while( True ):
        num = input(' ').lstrip().rstrip().strip()
        try:
            num = int( num )
            return num
        except Exception as e:
            num = None
   