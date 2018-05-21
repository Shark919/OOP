# -*- coding: utf-8 -*-
"""
Created on Sat May 19 14:24:51 2018

@author: D062400
"""

import random
import math

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

def my_quicksort(A, low, high):
    if low<high:
        m = partition_median(A, low, high)
        my_quicksort(A, low, m)
        my_quicksort(A, m+1, high)

def median(a, b, c):
    if ( a - b) * (c - a) >= 0:
        return a

    elif (b - a) * (c - b) >= 0:
        return b

    else:
        return c


def partition_median(array, leftend, rightend):
    left = array[leftend]
    right = array[rightend-1]
    length = rightend - leftend
    if length % 2 == 0:
        middle = array[leftend + length//2 - 1]
    else:
        middle = array[leftend + length//2]
  
    

    pivot = median(left, right, middle)

    pivotindex = array.index(pivot) #only works if all values in array unique

    array[pivotindex] = array[leftend]
    array[leftend] = pivot

    i = leftend + 1
    for j in range(leftend + 1, rightend):
        if array[j] < pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1

    leftendval = array[leftend]
    array[leftend] = array[i-1]
    array[i-1] = leftendval
    print(array)
    return i - 1 

def partition1(A,low,high):
#    pivot = my_pivot(A)
#    pivotIndex = 0
#    for i in range (low, high):
#        if A[i] == pivot:
#            pivotIndex = i
    pivotIndex = 5
    A[low], A[pivotIndex] = A[pivotIndex], A[low]
    
    pivot = A[low]
    i = low;
    for j in range(low+1,high+1):
        if( A[j] < pivot ):
            i=i+1
            A[i], A[j] = A[j], A[i]
    A[i], A[low] = A[low], A[i]
    return i
 
def my_pivot(list):
    elements = select_three_random_elements(list)
    return get_median(elements)

def select_three_random_elements(list):
    listLength = len(list)
    if(listLength > 2):
        elem1 = random.randint(0,listLength-1)
        elem2 = random.randint(0,listLength-1)
        while elem2 == elem1:
            elem2 = random.randint(0,listLength-1)
        elem3 = random.randint(0,listLength-1)
        while elem3 == elem1 or elem3 == elem2:
            elem3 = random.randint(0,listLength-1)
        return [list[elem1],list[elem2],list[elem3]]
    else:
        return list
    
def get_median(list):
    sortedList = sorted(list)
    return sortedList[math.floor(len(sortedList)/2)]

def test_my_quicksort():
    randlist = gen_randlist(1,10,10)
    print("random list is %s"  % randlist)
    my_quicksort(randlist, 0, 9)
    
# Konkrete Eingabe: [5,1,3,5], im folgenden als Tupel betrachtet:
# (5, "eins"), (1, ""), (3, ""), (5, "zwei")
# nach der Sortierung mit dem Quicksort Algorithmus sind die zwei fünfen
# nicht mehr in der Originalreihenfolge:
# (1, ""), (3, ""), (5, "zwei"), (5, "eins")
# damit ist der Sortieralgorithmus nicht stabil
# stabil wäre das Ergebnis: (1, ""), (3, ""), (5, "eins"), (5, "zwei")