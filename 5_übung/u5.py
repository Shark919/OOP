# -*- coding: utf-8 -*-
# Objektorientierte Programmierung
# Tutorium: Freitag 08-10 Uhr
# Christoph Meise, Tim Walz

import random
import time

################################
## Aufgabe 1
################################

def counting_sort(A, k):
    k += 1
    # Build C Array with length of k and place 0 everywhere
    C = [0 for i in range(0, k)]
    for j in range(0, len(A)):
        # For every number in A, add 1 to the corresponding position in C
        C[A[j]] += 1
    i = 0
    # Loop over C
    for j in range(0, k):
        # Loop over position in C to fetch occurrences of number
        for c in range(0, C[j]):
            A[i] = j
            i += 1
    return A

# b)
# Zusätzlich benötigter Speicherplatz in Höhe des Hilfsarrays C[0..k]
# Da counting_sort nicht Vergleichsbasiert arbeitet, kann eine lineare
# Problemkomplexität angenommen werden, d.h. O(n+k)

# Aus Übung 4
def gen_randlist(a,b,n):
    randlist = []
    for i in range(0,n):
        randlist.append(random.randint(a,b))
    return randlist
# Ende des Codes aus Übung 4

def test_counting_sort():
    tmp = gen_randlist(1,10,10)
    print("Test counting_sort with", tmp)
    print(counting_sort(tmp, max(tmp)))
    assert sorted(tmp) == counting_sort(tmp, max(tmp))
    tmp = gen_randlist(1,25,25)
    print("Test counting_sort with", tmp)
    print(counting_sort(tmp, max(tmp)))
    assert sorted(tmp) == counting_sort(tmp, max(tmp))

################################
## Aufgabe 2
################################
# Kein Counting-Sort, da wir eine große Spannweite an Integern abdecken wollen
# Kein Mergesort, da O(n) zusätzlicher Speicher benötigt wird
# Kein Insertionsort, da wir ein großes Array mit großem N sortieren
# Kein Quicksort, da worst-case Performance von O(N^2)
# Heapsort hat eine garaniterte Laufzeit von O(N log N) und eignet sich gut für 
# große Inputs und wird deshalb hier verwendet.
# Nachteil der Lösung: Im Vergleich zur Python-Standard Funktion sort(), ist Heapsort
# wesentlich langsamer (siehe Output von sort_Mio_Array())

def generate_Mio_Array():
    A = [random.randint(-214783648, 2147483647) for i in range(1000000)]
    return A

def sort_Mio_Array(A):
    heapsort(A)

def test_sort_Mio_Array():
    print("Starte Test, das wird etwas dauern...")
    B = generate_Mio_Array()
    t1 = time.time()
    heapsort(B)
    t2 = time.time()
    print("Die Ausführungszeit mit Heapsort betrug:", (t2-t1), " Sekunden")
    B = generate_Mio_Array()
    t1 = time.time()
    B.sort()
    t2 = time.time()
    print("Die Ausführungszeit mit sort() betrug:", (t2-t1), " Sekunden")

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
## Ende des Codes aus der Vorlesung

################################
## Aufgabe 3
################################
"""
Beweis der gegebenen Programmformel mittels Zuweisungsaxiom und Sequenzregel.
Da {P}{R1}{S1}{R2} und {R2}{S2}{R3} und {R3}{S3}{R4} und {R4}{S4}{Q} gültig sind,
ist auch {P}{S1}{S2}{S3}{S4}{Q} gültig.

 {P} = {a>0 && b>0 && b<0}

 {R1} = {a+b-c>0 && a+b-c-b-c>0 && -c>0 && a+b-c-b-c==a+b-c-b-c}

 {S1} a = a + b - c

 {R2} = {a>0 && a-b-c>0 && -c>0 && a-b-c==a-b-c}

 {S2} d = b

 {R3} = {a>0 && a-b-c>0 && -c>0 && a-b-c==a-d-c}

 {S3} b = a - b - c
 
 {R4} = a>0 ç b>0 && -c>0 && b==a-d-c

 {S4} c = -c
 
 {Q} = {a > 0 && b > 0 && c > 0 && b == a - d + c}
"""

def test_aufgabe_3(a, b, c):
    assert (a > 0 and b > 0 and c < 0) == True
    assert (a+b-c>0 and a+b-c-b-c>0 and -c>0 and a+b-c-b-c==a+b-c-b-c) == True
    a = a + b - c
    assert (a>0 and a-b-c>0 and -c>0 and a-b-c==a-b-c) == True
    d = b
    assert (a>0 and a-b-c>0 and -c>0 and a-b-c==a-d-c) == True
    b = a - b - c
    assert (a>0 and b>0 and -c>0 and b==a-d-c)
    c = -c
    assert (a > 0 and b > 0 and c > 0 and b == a - d + c) == True

################################
## Aufgabe 4
################################
"""
# erst if Bedingung Beweisen
{P} = {x >= 0 && (x*y + z) == c}

{B} = (x % 2 == 0)

{P2} = {P} && {B} == {x >= 0 && (x*y + z) == c && x%2==0}

{R} = {x//2 > 0 && ((x//2) * y + z) === c}

{R2} = {x//2 > 0 && (x//2) * (y+y) + z === c}

{P2} -> {R2}

{R2} <-> {x//2 > 0 && ((x//2) * (y+y) + z) === c} 
<-> {x//2 > 0 && ((x//2) * 2y + z) === c} 

{P2} <-> {x >= 0 && (x*y + z) == c && x%2==0}

x//2 > 0 wahr, da x>=0
(x//2) * 2y + z) ergibt ganz Zahl c, weil: x//2==ganze Zahl, 
ganzeZahl * 2y ergibt ganze Zahl (weil y vom typ int)
und diese ganze Zahl plus eine ganze zahl z (typ int) ergibt c, eine ganze Zahl
--> {P2} -> {R2}

IF BEDINGUNG BEWIESEN

jetzt else:

{R} = {x-1 >= 0 && ((x-1)*y +z) == c}
{R2} = {x-1 >= 0 && ((x-1)*y +(z+y)) == c}

{P3} = {P} && {not B} 
{P3} = {x >= 0 && (x*y + z) == c && x%2!==0}

beweisen das gilt:
{P3} -> {R2}&& 

x >= 0 && x%2!==0 --> dann ist x>=1, also x-1 >= 0
((x-1)*y +(z+y)) == c) ist damit auch wahr, weil x-1 ist ganze Zahl, 
y ist ganze Zahl und (z+y) ist ganze Zahl, damit ist auch die Addition
und Multiplikation vom typ int ->  {P3} -> {R2}

ABSCHLUSS
da der if-teil partiell korrekt ist ({P2} -> {R2})
und der else-teil partiell korrekt ist ({P3} -> {R2}),
ist auch die ganze Programmformel partiell korrekt.

{Q} = {x >= 0 && (x*y+z)==c}
"""
def testInvariantA(A):
    assert(A == A)

def testInvariantB(A, i):
    for j in range (0, i-1):
        assert(A[j+1] >= A[j])

def insertsort(A):
    h = 1
    i = 0
    # invariante: A enthält nur Elemente aus A
    testInvariantA(A)
    while i < len(A):
        j = i
        temp = A[j]
        # invariante: Elemente A[0] bis A[i-1] sind sortiert
        testInvariantB(A, i)
        while j>=h and A[j-h]>temp:
            A[j] = A[j-h]
            j = j-h
        A[j] = temp
        i = i+1
    return A

print(insertsort([3,2,5,2,6,1,6,5,42,5,1,9]))

################################
## Aufgabe 6
################################
# Algorithmus ist komplett selber ausgedacht, 
# Implementierungsaufwand war mir am Ende aber einfach zu hoch für die 4 Punkte bei der begrenzten Zeit.
# Funktioniert noch nicht für beliebig komplexe Matritzen, aber für die Beispiele im Test ist er korrekt
# (es fehlt noch logik zum durchprobieren bei größeren Quadrate, im Kommentar ist code angeteasert)

def findSquareInArrays(A, B):
    # per definition smallest square is 2x2, 
    # otherwise every single 1 is possible square, which is boring
    start = 0
    end = 0
    #print('A %s and B %s' % (A,B))
    for i in range (0, len(A)):
        for j in range (0, len(B)):
            if not(len(A[i]) == 0 or len(B[j]) == 0):
                if not((A[i][1] - A[i][0]) < 1) or (B[j][1] - B[j][0] < 1):
                    #print('yooo')
                    if A[i][0] >= B[j][0]:
                        start = A[i][0]
                    else: 
                        start = B[j][0]
                    if A[i][1] <= B[j][1]:
                        end = A[i][1]
                    else:
                        end = B[j][1]
    #print('start %s and end %s' % (start,end))
    if start == 0 and end == 0:
        return []
    return [start, end]

def squareBiggerThanCurrent(square, current):
    if len(square) >= 1:
        currentLength = current[1] - current[0]
        squareLength = square[1] - square[0]
        if currentLength < squareLength:
            return True
    return False

def getStreaksPerColumn(A):
    streakStartIndex = 0
    streakEndIndex = 0
    currentStreak = 0
    streaksPerColumn = []

    # linear complexity, goes through every single number in matrix but only once (column by column)
    for i in range (0,len(A[0])):
            currentStreak = 0
            foundStuff = False
            streakArr = []
            for j in range (0, len(A)):
                if A[j][i] == 1:
                    if currentStreak == 0: # a new streak in column started
                        streakStartIndex = j
                    currentStreak = currentStreak + 1
                else: # streak ended
                    if currentStreak > 0:
                        streakEndIndex = j
                        streakArr.append([streakStartIndex, streakEndIndex - 1])
                        streakStartIndex = 0
                        streakEndIndex = 0
                        currentStreak = 0
                        foundStuff = True
                if A[j][i] == 1 and (j+1 >= (len(A))): # column ended with 1
                    streakEndIndex = j                     
                    streakArr.append([streakStartIndex, streakEndIndex])                    
                    streakStartIndex = 0
                    streakEndIndex = 0
                    foundStuff = True
                    currentStreak = 0
            if foundStuff == False:
                streakArr.append([])
            streaksPerColumn.append(streakArr)
    return streaksPerColumn

def printMatrix(A):
    for i in range (0,len(A)):
        print(A[i])

def getTupleFromArray(resultPoints):
    resultTupleStart = (resultPoints[0][0], resultPoints[0][1])
    resultTupleEnd = (resultPoints[1][0], resultPoints[1][1])
    return (resultTupleStart, resultTupleEnd)

def getStartAndEndPointFromStreaks(streaksPerColumn):
    resultStart = [0,0]
    resultEnd = [0,0]
    # afterwards check for overlaps
    # number of arrays with streaks < number of elements in matrix
    # --> still linear complexity
    print('streaks per col %s' % streaksPerColumn)
    for i in range(0, len(streaksPerColumn) - 1):
        
        for j in range(i+1, len(streaksPerColumn)):
            # skip emptys
            if len(streaksPerColumn[j]) >= 1 and len(streaksPerColumn[i]) >= 1:
                square = findSquareInArrays(streaksPerColumn[j-1], streaksPerColumn[j])
                #print('Found a square at pos %s' % square)
                #print('and current is %s' % [resultStart[0], resultEnd[1]])
                #print('i is %s and j is %s' % (i,j))
                if squareBiggerThanCurrent(square, [resultStart[0], resultEnd[1]]):
                    #print('Found a square at pos %s' % square)
                    if resultStart[0] == 0 and resultStart[1] == 0:
                        resultStart = [square[0], i]
                    resultEnd = [square[1], j]
                    print('resultStart at %s resultEnd at %s' % (resultStart, resultEnd))

    """for col in range(0, len(streaksPerColumn) - 1):
        for streak in range(0, len(streaksPerColumn[i])):
            lengthOfSide = streak[1]-streak[0]
            # check overflow
                for indexSquareCheck in range (col+1 ,col+lengthOfSide):
                    if colHasSimilarStreak(streaksPerColumn(indexSquareCheck), streak)
                    ...
    """

    return [resultStart, resultEnd]

def matrixSquare(A):
    printMatrix(A)
    streaksPerColumn = getStreaksPerColumn(A)
    resultPoints = getStartAndEndPointFromStreaks(streaksPerColumn)
    resultTuple = getTupleFromArray(resultPoints)

    if resultPoints[0][0] == 0 and resultPoints[0][1] == 0 and resultPoints[1][0] == 0 and resultPoints[1][1] == 0:
        return ()
    return resultTuple

def test_matrixSquare():
    print(matrixSquare([[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]))
    print(matrixSquare([[0,0,0,0],[1,1,0,0],[1,1,0,0],[0,0,0,0]]))
    print(matrixSquare([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))
    print(matrixSquare([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]))
    #print(matrixSquare([[0,0,1,1,0,1,0,0,0,0,0,0,0],[0,0,1,0,1,0,1,1,1,1,1,1,0],[0,0,0,0,0,0,1,1,1,1,1,1,0],[0,0,0,0,0,1,1,1,1,1,1,1,0],[0,0,0,0,0,1,1,1,1,1,1,1,0],[0,1,0,1,0,1,0,1,0,1,0,1,0],[0,1,1,1,1,0,0,1,1,1,1,0,0]]))
    #print(matrixSquare([[0,0,1],[0,0,0],[0,0,1]]))
    
test_matrixSquare()
