# -*- coding: utf-8 -*-
# Objektorientierte Programmierung
# Tutorium: Freitag 08-10 Uhr
# Christoph Meise, Tim Walz

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

# Aufgabe 4

def merge_sort(A):
    
    unit = 1
    while unit <= len(A):
        h = 0
        for h in range(0, len(A), unit * 2):
            l, r = h, min(len(A), h + 2 * unit)
            mid = h + unit
            # merge A[h:h + 2 * unit]
            p, q = l, mid
            while p < mid and q < r:
                if A[p] < A[q]: p += 1
                else:
                    tmp = A[q]
                    A[p + 1: q + 1] = A[p:q]
                    A[p] = tmp
                    p, mid, q = p + 1, mid + 1, q + 1
        unit *= 2
    return A

# Aufgabe 5
# a) Angenommen folgendes Arrray in max-heap format [22, 19a, 19b, 12, 10, 8, 5]
# 19a = 19b. a und b repraesentieren nur die Reihenfolge. 
# Im ersten Schritt wird 22 an den letzten Index geschoben
# Dann wird 19a an den vorletzen und 19b an den vorvorletzen Index verschoben
# Fertige Sortierung: [5, 8, 10, 12, 19b, 19a, 22]
# Die Reihenfolge von 19a und 19b wird verändert -> Algorithmus ist nicht stabil

# b) Die Komplexität des Heapsort Algorithmus ist immer O(n log n). Es benötigt
# O(n) Zeit das max-heap zu bauen. Zum Sortieren wird nun immer das erste Element
# an den letzten Index verschoben und auf den Rest heapify aufgerufen. Dies wird
# n-Male wiederholt. Für alle Schritte wird also O(n log n) Zeit benötigt.

# c)

def is_max_heap(A):
    for head in range(0, len(A)):
        c1, c2 = head * 2+ 1, head * 2 + 2
        if c1 < len(A) and A[head] < A[c1]:
            return False
        if c2 < len(A)and A[head] < A[c2]:
            return False
    return True

## Testing Section 

# Neue Implementierung der is_sort Funktion, da Name != Aufgabe 2 is_sorted
def is_sort(l):
    return all(l[i] <= l[i+1] for i in range(len(l)-1))

def test_merge_sort():
    assert is_sort(merge_sort(gen_randlist(1, 50, 42))) == True
    assert is_sort(merge_sort(gen_randlist(1, 50, 24))) == True

def test_is_max_heap():
    assert is_max_heap([90, 15, 10, 7, 12, 2]) == True
    assert is_max_heap([34, 25, 10, 16, 17, 7, 44, 49, 38, 26, 36, 9, 27, 8, 27, 25, 33, 21, 33, 21, 5, 27, 39, 8, 34, 8, 29, 19, 44, 10, 13, 45, 40, 48, 46, 46, 14, 3, 6, 38, 1, 21]) == False