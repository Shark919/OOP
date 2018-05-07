import math
import time
import random

# 1. Aufgabe
def apply_if(f, p, xs):
    # assumes f, p is a function and xs is a list
    res = []
    for x in xs:
        if p(x) == True:
            res.append(f(x))
        else:
            res.append(x)
    return res

# Hilfsfunktion für 1. Aufgabe
def odd(x):
    if x % 2 == 1:
        return True
    else:
        return False

# Testmethode der 1. Aufgabe
def test_apply_if():
    if apply_if(math.factorial, odd, [2,5,7,4,9,6]) == [2, 120, 5040, 4, 362880, 6]:
        print("Test bestanden")
    else:
        print("Test nicht bestanden")

# 2. Aufgabe Teil a
def zipWith(f, xs, ys):
    # assumes xs, ys are lists
    if len(xs) == 1 or len(ys) == 1:
        return [f(xs[0], ys[0])]
    else:
        return [f(xs[0], ys[0])] + zipWith(f, xs[1:], ys[1:])

# 2. Aufgabe Teil b
def zipWith2(f, xs, ys):
    # assumes xs, ys are lists
    res = [f(a,b) for (a,b) in zip(xs, ys)]
    return res

# Testmethode der 2. Aufgabe inkl. Teil c
def test_zipWith():
    start = time.time()
    test1 = zipWith(divmod, [1,2,3,15], [1,2,3,4])
    end = time.time()
    if test1 == [(1, 0), (1, 0), (1, 0), (3, 3)]:
        print("Test zipWith bestanden, die Ausführungszeit betrug:", (end-start))
    else:
        print("Test zipWith nicht bestanden, die Ausführungszeit betrug:", (end-start))

    start = time.time()
    test2 = zipWith2(divmod, [1,2,3,15], [1,2,3,4])
    end = time.time()
    if test2 == [(1, 0), (1, 0), (1, 0), (3, 3)]:
        print("Test zipWith2 bestanden, die Ausführungszeit betrug:", (end-start))
    else:
        print("Test zipWith2 nicht bestanden, die Ausführungszeit betrug:", (end-start))

# 3. Aufgabe
def my_random(lower, upper):
    i = 0
    dictionary = {}
    x = random.randint(lower, upper)
    while str(x) not in dictionary:
        dictionary[str(x)] = 1
        x = random.randint(lower, upper)
        i += 1
    return i

# Testmethode der 3. Aufgabe
def test_my_random():
    lower = -100
    upper = 100
    if my_random(lower, upper) > 0:
        print("Test my_random bestanden")
    else:
        print("Test my_random nicht bestanden")

# 4. Aufgabe Teil a
def double_birthday():
    i = 1
    birthdays = {}
    birthday = createBD
    while birthday not in birthdays:
        birthdays[birthday] = 1
        i +=1
        birthday = createBD()
    return i

# Hilfsfunktion zum generieren von Geburtstagen für Teil a
def createBD():
    year = random.randint(1940, 2017)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return str(day).zfill(2) + str(month).zfill(2) + str(year)

# Testmethode der 4. Aufgabe Teil a
def test_double_birthday():
    if double_birthday() > 0:
        print("Test double_birthday bestanden")
    else:
        print("Test double_birthday nicht bestanden")

# Aufgabe 4 Teil b
def repeat_double_birthday():
    duplicates = []
    i = 0
    while i < 1000:
        bd = double_birthday()
        if bd > 365:
            pass
        else: 
            duplicates.append(bd)
        i +=1
    return duplicates

# Testmethode der 4. Aufgabe Teil b
def test_repeat_double_birthday():
    result = repeat_double_birthday()
    if len(result) > 0:
        print("Test repeat_double_birthday bestanden")
    else:
        print("Test repeat_double_birthday nicht bestanden")

# Aufgabe 4 Teil c
#def birthday_paradox(n):
#    listOfDuplicates = []
#    for x in range(0, n):
#        duplicates = repeat_double_birthday()
#        listOfDuplicates.append(duplicates)
#    numberOfDuplicates = 0
#    for x in range(0, listOfDuplicates.count()):
#        for y in range(0, listOfDuplicates[x].count())
#        listOfDuplicates[x][]
#    duplicates = repeat_double_birthday()
#    if str(n) in duplicates:
#        res = duplicates
#        return "Die Wahrscheinlichkeit liegt bei " + duplicates[str(n)] + "%."
#    else:
#        return "Kein Datensatz vorhanden!"
