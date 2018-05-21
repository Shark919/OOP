# -*- coding: utf-8 -*-
"""
Created on Sat May 19 14:24:51 2018

@author: D062400
"""

import random

# Aufgabe 1
# 1a)
# Maximale Länge der Liste ist 999,
# Ab 1000 ist die maximale Rekustionstiefe erreicht
# "Maximum recursion depth of 999 reached"
# kann aber auch erhöht werden -> sys.setrecursionlimit(1500)
# 1b)
# Maximale Länger der List 999² = 998001
# 1c)
# Bei der linearer Suche erhöht sich die Rekusionstiefe bei jedem
# Listenelement um 1, damit max depth bei Länge 1000
# binäre Suche hat O(log n) und damit erhöht sich die Rekursionstiefe
# nicht linear, sondern logarithmisch -> maximale Länge = n², n=Länge der Liste

# Aufgabe 2
def is_sorted(list):
    i = 0
    isSorted = True
    while i < len(list)-1:
        if list[i+1] < list[i]:
            isSorted = False
        i += 1
    return isSorted

def gen_randlist(a,b,n):
    randlist = []
    for i in range(0,n):
        randlist.append(random.randint(a,b))
    return randlist

# Aufgabe 3
# 3a)
# O Notationen: Insertionsort O(n^2) > Quicksort O(nlogn)
# O Notation ist jedoch eine Approximation des asymptotische Verhaltens für große n
# Insertionsort ist schneller für kleine n, weil es weniger overhead hat, 
# als Quicksort mit den rekursiven Funktionsaufrufen
# Insertionsort ist auch stabiler als Quicksort und braucht weniger Speicher

def sort(A):
    my_quicksort(A, 0, len(A) -1)
    return A

def my_quicksort(A, low, high):
    if low<high:
        m = partition(A, low, high)
        my_quicksort(A, low, m)
        my_quicksort(A, m+1, high)

def partition(A, low, high):
    pivotIndex = pivot_median(A, low, high)
    pivot = A[pivotIndex]
    A[pivotIndex], A[low] = A[low], A[pivotIndex]
    i = low
    for j in range(low+1,high+1):
        if ( A[j] < pivot ):
            i=i+1
            A[i], A[j] = A[j], A[i]
    A[i], A[low] = A[low], A[i]
    return i
 
def pivot_median(A, low, high):
    mid = (high + low) // 2
    s = sorted([A[low], A[mid], A[high]])
    if s[1] == A[low]:
        return low
    elif s[1] == A[mid]:
        return mid
    return high

def test_my_quicksort():
    randlist = gen_randlist(1,10,10)
    print("random list is %s"  % randlist)
    print("sorted list is %s" % sort(randlist))
    
# Konkrete Eingabe: [5,1,3,5], im folgenden als Tupel betrachtet:
# (5, "eins"), (1, ""), (3, ""), (5, "zwei")
# nach der Sortierung mit dem Quicksort Algorithmus sind die zwei fünfen
# nicht mehr in der Originalreihenfolge:
# (1, ""), (3, ""), (5, "zwei"), (5, "eins")
# damit ist der Sortieralgorithmus nicht stabil
# stabil wäre das Ergebnis: (1, ""), (3, ""), (5, "eins"), (5, "zwei")