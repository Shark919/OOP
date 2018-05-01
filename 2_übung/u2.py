#import math
#import operator
import time
import random

def apply_if(f, p, xs):
    # assumes f, p is a function and xs is a list
    res = []
    for x in xs:
        if p(x) == True:
            res.append(f(x))
        else:
            res.append(x)
    return res

def odd(x):
    if x % 2 == 1:
        return True
    else:
        return False

# Rekursion fehlt noch

def zipWith2(f, xs, ys):
    # assumes xs, ys is a list
    res = [f(a,b) for (a,b) in zip(xs, ys)]
    return res

def myRandom(lower, upper):
    i = 0
    dictionary = {}
    while str(random.randint(lower, upper)) not in dictionary:
        dictionary[str(random.randint(lower, upper))] = 1
        i += 1
    return i

def double_birthday():
    i = 1
    birthdays = {}
    birthday = createBD
    while birthday not in birthdays:
        birthdays[birthday] = 1
        i +=1
        birthday = createBD()
    return i

def createBD():
    year = random.randint(1940, 2017)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return str(day).zfill(2) + str(month).zfill(2) + str(year)

def repeat_double_birthday():
    duplicates = {}
    i = 0
    while i < 365:
        num = str(double_birthday())
        if num not in duplicates:
            duplicates[num] = 1
        else:
            duplicates[num] += 1
        i +=1 
    return duplicates

# stimmt noch nicht
#def birthday_paradox(n):
#    duplicates = repeat_double_birthday()
#    if str(n) in duplicates:
#        res = duplicates
#        return "Die Wahrscheinlichkeit liegt bei " + duplicates[str(n)] + "%."
#    else:
#        return "Kein Datensatz vorhanden!"