# Objektorientierte Programmierung
# Tutorium: Freitag 08-10 Uhr
# Christoph Meise, Tim Walz

# Berechnet Produkt einer eingegebenen Liste
def multList( inputList ):
    res = 1
    for x in inputList:
        res = res * x
    return res

# Bestimmt alle echten Teiler eines eingegebenen Integers
def echtTeiler( number ):
    res = []
    for x in range ( 1, number ):
        if number % x == 0:
            res.append( x )
    return res

# Bestimmt, ob zwei Zahlen ein befreundetes Zahlenpaar sind
# Gibt für wahr 1 und falsch 0 zurück
def findFriend( in1, in2 ):
    res = bool(0)
    if in1 == sum(echtTeiler(in2)):
        res = bool(1)
    return res
        
def testMultList():
    if multList([1,2,4,5,6]) == 240:
        print("multList Test1 bestanden")
    else:
        print("multList Test1 nicht bestanden")

    if multList([4,5,6]) == 120:
        print("multList Test2 bestanden")
    else:
        print("multList Test2 nicht bestanden")

def testEchtTeiler():
    if echtTeiler(250) == [1, 2, 5, 10, 25, 50, 125]:
        print("echtTeiler Test1 bestanden")
    else:
        print("echtTeiler Test1 nicht bestanden")

    if echtTeiler(15) == [1, 3, 5]:
        print("echtTeiler Test2 bestanden")
    else:
        print("echtTeiler Test2 nicht bestanden")

def testFindFriend():
    if findFriend(1210,1184) == True:
        print("findFriend Test1 bestanden")
    else:
        print("findFriend Test1 nicht bestanden")
        
    if findFriend(220,284) == True:
        print("findFriend Test2 bestanden")
    else:
        print("findFriend Test2 nicht bestanden")
        
    if findFriend(284,220) == True:
        print("findFriend Test3 bestanden")
    else:
        print("findFriend Test3 nicht bestanden")
        
    if findFriend(3,3) == False:
        print("findFriend Test4 bestanden")
    else:
        print("findFriend Test4 nicht bestanden")

    
    
