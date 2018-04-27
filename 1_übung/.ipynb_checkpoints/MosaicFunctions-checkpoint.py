#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Version 0.3 Veranstaltung: Objektorientierte Programmierung
# Author: Prof. Dr. Margarita Esponda

"""	In this homework you have to program the inside of six diferent 'decide_color_..' functions.
        The functions calculate and returns a color for each (x,y) position of a square of side = size.
        
        The functions are used in the modul'MosaicFrames.py' which shows the diferent pictures (mosaics)
        on a window.
        
        We wrote some simple examples of decide_color functions
        Please overwrite them with your own solutions.

        The 'MosaicFrames.py' file and this file have to be in the same directory and you must start the programm
        with 'MosaicFrames.py'.
"""


def decide_color_squares(x, y, size):
    # overwrite the content of the function
    if x in range(100,199) and y in range(100,199):
        return 'RED'
    elif x in range(200,299) and y in range(200,299):
        return 'RED'
    else:
        return 'BLACK'

def decide_color_diags(x, y, size):
    # overwrite the content of the function
    if x==y:
        return 'RED'
    else:
        return 'YELLOW'

def decide_color_triangles(x, y, size):
    # overwrite the content of the function
    if x > 199 and y < 200:
        return 'GRAY'
    if x > 199 and y > 199:
        return 'GREEN'
    return 'BLUE'

def decide_color_circle(x, y, size):
    # overwrite the content of the function
    if x in range(0,199):
        return 'BLUE'
    return 'GRAY'

def decide_color_chess(x, y, size):
    # overwrite the content of the function
    if (x//50) % 2 == 0 and (y//50) % 2 == 0:
        return 'BLACK'
    if (x//50) % 2 == 1 and (y//50) % 2 == 1:
        return 'BLACK'
    else:
        return 'WHITE'

def decide_color_illusion_1(x, y, size):
    # overwrite the content of the function
    return "WHITE"

def decide_color_illusion_2(x, y, size):
    # overwrite the content of the function
    return "black"

def decide_color_illusion_3(x, y, size):
    # overwrite the content of the function
    return 'WHITE'

def decide_color_own_picture(x, y, size):
    return 'GRAY'
