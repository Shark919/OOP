# -*- coding: utf-8 -*-
# Objektorientierte Programmierung
# Tutorium: Freitag 08-10 Uhr
# Christoph Meise, Tim Walz

import numpy

# 1. Aufgabe
def is_max_heap(A):
    for head in range(0, len(A)):
        c1, c2 = head * 2+ 1, head * 2 + 2
        if c1 < len(A) and A[head] < A[c1]:
            return False
        if c2 < len(A)and A[head] < A[c2]:
            return False
    return True

# 2. Aufgabe

def counting_sort(A, k):
    k += 1
    C = [0] * k                 # init with 0
    for a in A:
        C[a] += 1               # count occurences
    i = 0
    for a in range(k):
        for c in range(C[a]):
            A[i] = a
            i += 1
    return A

# 3. Aufgabe

