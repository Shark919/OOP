import random

# 1. Aufgabe
def countChar(imp):
    res = {}
    # Iteriere über imp
    for x in imp:
        # Wenn x in imp addiere +1, sonst setze 1
        if x in res:
            res[x] = res.get(x) + 1
        else:
            res[x] = 1
    return res

# 3. Aufgabe
def createField(height, width):
    return [[0 for x in range(width)] for y in range (height)]

def printSpielFeld(imp):
    for x in imp:
        print(*x, sep=" ")

def newSpiel(matrix, p):
    i,j = 0,0
    for x in matrix:
        for y in x:
            if random.uniform(0,1) <= p:
                matrix[i][j] = 'O'
            else:
                matrix[i][j] = '.'
            j += 1
        i += 1
        j = 0
    return matrix

def generateSolution(matrix):
    i,j = 0,0

    height = len(matrix)
    width = len(matrix[0])
    for x in matrix:
        for y in x:
            if matrix[i][j] != 'O':  
                if i + 1 < height and matrix[i+1][j] == 'O':
                    matrix[i][j] = addOne(matrix[i][j])
                if i + 2 < height and matrix[i+2][j] == 'O':
                    matrix[i][j] = addOne(matrix[i][j])
                if i - 1 >= 0 and matrix[i-1][j] == 'O':
                    matrix[i][j] = addOne(matrix[i][j])
                if i - 2 >= 0 and matrix[i-2][j] == 'O':
                    matrix[i][j] = addOne(matrix[i][j])
                if j + 1 < width and matrix[i][j+1] == 'O':
                    matrix[i][j] = addOne(matrix[i][j])
                if j + 2 < width and matrix[i][j+2] == 'O':
                    matrix[i][j] = addOne(matrix[i][j])
                if j - 1 >= 0 and matrix[i][j-1] == 'O':
                    matrix[i][j] = addOne(matrix[i][j])
                if j - 2 >= 0 and matrix[i][j-2] == 'O':
                    matrix[i][j] = addOne(matrix[i][j])
            j += 1
        i += 1
        j = 0
    return matrix

def addOne(x):
    if x == '.':
        return 1
    else: return x+1