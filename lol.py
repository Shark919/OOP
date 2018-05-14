# -*- coding: utf-8 -*-
"""
Created on Fri May 11 09:18:26 2018

@author: D062400
"""

def collatz(n):
    liste = []
    for i in range(1, n):
        innerListe = []
        while i > 1:
            if (i % 2) == 0:
                i = i / 2
            else:
                i = i*3 + 1
            innerListe.append(i)
        liste.append(innerListe)
    return liste

