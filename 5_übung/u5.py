# -*- coding: utf-8 -*-
# Objektorientierte Programmierung
# Tutorium: Freitag 08-10 Uhr
# Christoph Meise, Tim Walz

import random
import time

# 1. Aufgabe

def counting_sort(A, k):
    k += 1
    C = [0 for i in range(0, k)]
    for j in range(0, len(A)):
        C[A[j]] += 1
    i = 0
    for j in range(0, k):
        for c in range(0, C[j]):
            A[i] = j
            i += 1
    return A

# 2. Aufgabe

# Kein Counting-Sort, da wir eine große Spannweite an Integern abdecken wollen
# Kein Mergesort, da recht viel O(n) zusätzlicher Speicher benötigt
# Kein Insertionsort, da wir ein großes mit großem N sortieren
# Kein Quicksort, da worst-case Performance von O(N^2)
# Heapsort hat eine garaniterte Laufzeit von O(N log N) und eignet sich gut für 
# große Inputs und wird deshalb hier verwendet.
# Nachteil der Lösung: Im Vergleich zur Python-Standard Funktion sort(), ist Heapsort
# wesentlich langsamer (siehe Output von sort_Mio_Array())

def generate_Mio_Array():
    A = [random.randint(-214783648, 2147483647) for i in range(1000000)]
    return A

def sort_Mio_Array(A):
    B = list(A)
    t1 = time.time()
    heapsort(A)
    t2 = time.time()
    print("Die Ausführungszeit mit Heapsort betrug:", (t2-t1))
    t1 = time.time()
    B.sort()
    t2 = time.time()
    print("Die Ausführungszeit mit sort() betrug:", (t2-t1))

## Verwenden der Heapsort Funktionen aus der Vorlesung
def max_heapify (H, pos): 
    left_t = left (pos)
    right_t = right(pos)
    if left_t<=heap_size(H) and H[left_t]>H[pos]:
        biggest = left_t
    else:
        biggest = pos
    if right_t<=heap_size(H) and H[right_t]>H[biggest]:
        biggest = right_t
    if biggest != pos:
        H[pos], H[biggest] = H[biggest], H[pos]
        max_heapify( H, biggest )
    
def build_max_heap(H):
    H[0] = len(H)-1
    for i in range(heap_size(H)//2, 0, -1):
        max_heapify( H, i )

def heap_size(H):
    return H[0]

def dec_heap_size(H): 
    H[0] = H[0]-1

def heapsort(H): 
    build_max_heap(H)
    for i in range( heap_size(H), 1, -1):
        H[i], H[1] = H[1], H[i]
        dec_heap_size(H)
        max_heapify( H, 1 )
    dec_heap_size(H)

def left(i):
    return i*2

def right(i): 
    return i*2+1


# 3. Aufgabe

def aufgabe_3():
    a = 10 
    b = 10
    c = -1000
    assert (a > 0 and b > 0 and c < 0) == True
    a = a + b - c
    d = b
    print(a, b, c)
    b = a - b - c
    print(b)
    c = -c
    assert (a > 0 and b > 0 and c > 0 and b == a - d + c) == True