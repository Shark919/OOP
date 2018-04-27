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

import random
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
    if (x%40)==(y%40):
        return 'RED'
    else:
        return 'YELLOW'

def decide_color_triangles(x, y, size):
    # overwrite the content of the function
    if x > (size-1)/2 and y < size/2:
        if size - x < y:
            return 'WHITE'
        else:
            return 'GRAY'
    if x > (size-1)/2 and y > (size-1)/2:
        if x > y:
            return 'WHITE'
        else:
            return 'GREEN'
    sizeSmall = int(size / 6)
    if x in range(sizeSmall,sizeSmall*2) and y in range(sizeSmall*4, sizeSmall*5):
        x = x - sizeSmall
        y = y - sizeSmall*4
        if sizeSmall-x < y:
            return 'GREEN'
        else:
            return 'ORANGE'
    return 'BLUE'

def decide_color_circle(x, y, size):
    # overwrite the content of the function
    if ((x-200)**2 +  (y-200)**2) < 105625 and ((x-200)**2 +  (y-200)**2) > 40000 and x < size/2:
        return 'WHITE'
    elif ((x-200)**2 +  (y-200)**2) < 105625 and ((x-200)**2 +  (y-200)**2) > 40000 and x > size/2:
        return 'RED'
    elif x in range(0,199):
        return 'BLUE'
    return 'GRAY'

def decide_color_chess(x, y, size):
    # overwrite the content of the function
    size = size / 8
    if (x//size) % 2 == 0 and (y//size) % 2 == 0:
        return 'BLACK'
    if (x//size) % 2 == 1 and (y//size) % 2 == 1:
        return 'BLACK'
    else:
        return 'WHITE'

def decide_color_illusion_1(x, y, size):
    # overwrite the content of the function
    if x in range(150,250) and y in range(150,250):
        return 'PURPLE'
    elif (x//5) % 4 == 0 or (y//5) % 4 == 0:
        return 'WHITE'
    else:
        return "BLACK"

def decide_color_illusion_2(x, y, size):
    # overwrite the content of the function
    if (x//5) % 4 == 0 and (y//5) % 4 == 0:
        return 'WHITE'
    elif (x//5) % 4 == 0 or (y//5) % 4 == 0:
        return 'GREY'
    else:
        return "BLACK"

def decide_color_illusion_3(x, y, size):
    # overwrite the content of the function
    if (y//2) % 12 == 0:
        return 'GREY'
    elif ((x+(((y//24+2)*7)%3))//24) % 2 == 0 and (y//24) % 2 == 0:
        return 'BLACK'
    elif ((x++(((y//24+2)*7)%3))//24) % 2 == 0 and (y//24) % 2 == 1:
        return 'BLACK'
    return 'WHITE'

def decide_color_own_picture(x, y, size):
    mycolors = ['WHITE','GREY','PINK','RED','BLUE','PURPLE','ORANGE']
    if 1 == 1:
        return mycolors[random.randint(0, 6)]
    return 'GRAY'
