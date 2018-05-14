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

# 2. Aufgabe
# Aufgabe 2a
def gossip(m):
    # because spreading gossip doesn't make any sense with less than 3 ppl
    if m < 3:
        return {}
    guestList = initializeGuestList(m)
    gossipStarter = random.randint(0,m-1)
    #print('Guest number %s started the gossip - nobody likes you' % gossipStarter)
    guestList[gossipStarter] = True
    gossipAbout = randomNumberInRangeButNot(len(guestList)-1, gossipStarter)
    #print('Guest number %s is the gossip victim...poor guy' % gossipAbout)
    spreadGossip(guestList, gossipStarter, gossipAbout)
    #print('This is the guest list: %s' % guestList)
    return guestList

def initializeGuestList(m):
    guestList = {}
    for i in range (0,m):
        guestList[i] = False
    return guestList
    
def spreadGossip(guestList, gossipStarter, gossipAbout):
    gossipReceiver = randomNumberInRangeButNot(len(guestList)-1, gossipAbout)
    #print('Guest number %s shared the gossip with %s' % (gossipStarter, gossipReceiver))
    if guestList[gossipReceiver] == False:
        guestList[gossipReceiver] = True
        spreadGossip(guestList, gossipReceiver, gossipAbout)

def randomNumberInRangeButNot(length, notThisNumber):
    result = random.randint(0,length)
    if result == notThisNumber:
        result = randomNumberInRangeButNot(length, notThisNumber)
    return result

# Aufgabe 2b
def sim_gossip(m, n):
    average = 0
    for i in range(0, n-1):
        guestList = gossip(m)
        gossipKnowers = getNumberOfKnowers(guestList)
        average = average + gossipKnowers
    return (average / n) - 1 # minus the person who initiated the gossip
        
   
def getNumberOfKnowers(guestList):
    gossipKnowers = 0
    for guest in guestList.values():
        if guest == True:
            gossipKnowers += 1
    return gossipKnowers

def all_get_gossip(m):
    trys = 1000000
    numberOfTimesAllGuestsKnew = 0
    for i in range (0, trys):
        guestList = gossip(m)
        numberOfKnowers = getNumberOfKnowers(guestList)
        if numberOfKnowers == m-1:
            numberOfTimesAllGuestsKnew += 1
    return (numberOfTimesAllGuestsKnew / trys)*100
        
def test_gossip():
    print('With 1 guest: %s' % gossip(1))
    print('With 10 guests: %s' % gossip(10))

def test_sim_gossip():
    print('be patient, this takes a few seconds...')
    print('Average number of gossip receivers is %s' % sim_gossip(5, 1000000))
    
def test_all_get_gossip():
    print('be patient, this takes a few seconds...')
    print('Chances that all know about gossip are %s percent' % all_get_gossip(10))
    
    
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