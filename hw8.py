#################################################
# hw8.py:
#
# Your name: alanis zhao
# Your andrew id: aazhao
#################################################

import cs112_s22_week8_linter
from cmu_112_graphics import *

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Midterm1 Free Responses
#################################################
def checkSquare(n1,n2): #checks if the square of 1 number = other number
    if (n1**2==n2):
        return True
    return False

def lenNum(n): #finds num digits of n
    digs=0
    while(n>0):
        digs+=1
        n//=10
    return digs

def isPreSquareNumber(n): #checks if a number is presquare
    if(n<0):
        return False
    for currEnd in range(1,lenNum(n)): #loops through poss r and l combos
        end=n%10**currEnd
        beg=n//10**currEnd
        if(checkSquare(beg,end)):
            return True
    return False

def nearestPreSquareNumber(n): #finds nearest presquare num to n
    if (isPreSquareNumber(n)): #return n if its presquare
        return n
    check=1
    found=False
    while(found!=True): #loops through closest numbers to n
        before=n-check 
        after=n+check
        beforePre,afterPre=False,False
        if(isPreSquareNumber(before)): #checks if before is pre
            beforePre=True
        if(isPreSquareNumber(after)): #checks if after is pre
            afterPre=True
        if(beforePre and afterPre or beforePre):
            #returns after if both are true or only after is true
            return before
        elif(afterPre):
            return after
        else: #keeps looping
            check+=1

def getRecord(team, scores): #returns tuple of w/l/t
    games=[]
    for currLine in scores.splitlines(): #adds all of team games to list
        if(team in currLine):
            games.append(currLine)
    wins=0
    losses=0
    ties=0
    for game in games: #runs through each game
        score=0
        otherScore=0
        teamI=0
        otherI=0
        sep=ridSpaces(game) #list of all words with no spaces
        for curr in range(len(sep)):
            if(sep[curr]==team): #finds team index in list
                teamI=curr
            elif(sep[curr].isalpha()): #finds other team's index in list
                otherI=curr
        score=int(sep[teamI+1]) #finds team score
        otherScore=int(sep[otherI+1]) #finds other team's score
        #below adds to w/l/t
        if(score>otherScore):
            wins+=1
        elif(otherScore>score):
            losses+=1
        else:
            ties+=1
    return (wins,losses,ties)

def ridSpaces(s): #turns string into list w no spaces
    ret=[]
    for curr in s.split(' '):
        ret.append(curr)
    return ret

#################################################
# Other Classes and Functions for you to write
#################################################

class Person(object): #defines class of person
    def __init__(self, name, age): #creates person
        self.name=name
        self.age=age
        self.friends=[]
        self.friendNames=[]
    def getName(self): #returns name
        return self.name
    def getAge(self): #returns age
        return self.age
    def getFriends(self): #returns list of non-rep friends
        return self.friends
    def getFriendsNames(self): #returns sorted list of non-rep friend names
        return sorted(self.friendNames)
    def addFriend(self,person): #adds friend
        if(person not in self.friends): #checks if repeat
            self.friends.append(person)
            person.friends.append(self) #mutual
        if(person.getName() not in self.friendNames): #checks if repeat
            self.friendNames.append(person.getName())
            person.friendNames.append(self.getName()) #mutual
    def addFriends(self,person): #adds all of person's friends
        for curr in person.friends:
            if(curr not in self.friends): #checks if repeat
                self.friends.append(curr)
            if(curr.getName() not in self.friendNames): #checks if repeat
                self.friendNames.append(curr.getName())

def getPairSum(L, target): #returns pair of ints in L that add to target
    curr = set()
    curr.add(1)
    print(curr)
    Lset = set()
    for currNum in L: #runs through list
        if(currNum in Lset and currNum*2==target): #checks if # is twice in L
            return (currNum,currNum)
        else: #checks if corresponding # in Lset
            check = target-currNum
            if check in Lset:
                return (check,currNum)
            Lset.add(currNum)
    return None

def containsPythagoreanTriple(L): #returns if list has pyth triple
    Lset = set(L)
    for n1 in Lset: #loops through first number
        for n2 in Lset: #loops through second number
            if(n1!=n2):
                c = retTrip(n1,n2)
                if (c in Lset and c!=n1): #if corresponding # in list
                    return True
    return False

def retTrip(a,b): #returns c that corresponds to given a and b
    c2 = a**2+b**2
    return c2**0.5

def movieAwards(oscarResults): #returns dict of movie names w # wins
    movies = {}
    for currMovie in oscarResults: #loops through movies in dict
        if currMovie[1] in movies:
            movies[currMovie[1]]+=1
        else:
            movies[currMovie[1]]=1
    return movies

def friendsOfFriends(friends): #returns friends of friends for each person
    friendsOFriends = {}
    for person in friends: #loops through initial person
        friendsOFriends[person]=set()
        for checkFriend in friends[person]: #loops through their friends
            for fof in friends[checkFriend]: #checks friends of friends
                if(person!=fof and fof not in friends[person]):
                    friendsOFriends[person].add(fof)
    return friendsOFriends

#################################################
# Bonus Animation
#################################################

def appStarted(app):
    app.level = 1

def drawSierpinskiTriangle(app, canvas, level, x, y, size):
    # (x,y) is the lower-left corner of the triangle
    # size is the length of a side
    # Need a bit of trig to calculate the top point
    if level == 0:
        topY = y - (size**2 - (size/2)**2)**0.5
        canvas.create_polygon(x, y, x+size, y, x+size/2, topY, fill='black')
    else:
        # Bottom-left triangle
        drawSierpinskiTriangle(app, canvas, level-1, x, y, size/2)
        # Bottom-right triangle
        drawSierpinskiTriangle(app, canvas, level-1, x+size/2, y, size/2)
        # Top triangle
        midY = y - ((size/2)**2 - (size/4)**2)**0.5
        drawSierpinskiTriangle(app, canvas, level-1, x+size/4, midY, size/2)

def keyPressed(app, event):
    if event.key in ['Up', 'Right']:
        app.level += 1
    elif (event.key in ['Down', 'Left']) and (app.level > 0):
        app.level -= 1

def redrawAll(app, canvas):
    margin = min(app.width, app.height)//10
    x, y = margin, app.height-margin
    size = min(app.width, app.height) - 2*margin
    drawSierpinskiTriangle(app, canvas, app.level, x, y, size)
    canvas.create_text(app.width/2, 0,
                       text = f'Level {app.level} Fractal',
                       font = 'Arial ' + str(int(margin/3)) + ' bold',
                       anchor='n')
    canvas.create_text(app.width/2, margin,
                       text = 'Use arrows to change level',
                       font = 'Arial ' + str(int(margin/4)),
                       anchor='s')

runApp(width=400, height=400)

#################################################
# Test Functions
#################################################

def testNearestPreSquareNumber():
    print('Testing nearestPreSquareNumber(n)...', end='')
    assert(nearestPreSquareNumber(0) == 11)
    assert(nearestPreSquareNumber(6000) == 6036)
    assert(nearestPreSquareNumber(-100) == 11)
    #Negatives should still work
    assert(nearestPreSquareNumber(20202) == 20004)
    #Halfway between 20004 and 20400
    assert(nearestPreSquareNumber(30100) == 30009)
    #Some solutions may be too slow!
    print('Passed!')

def testGetRecord():
    print('Testing getRecord()...', end='')
    scores = '''\
    Chi 2 - Pit 1
    Chi 2 - Pit 11
    Mia 13 - Pit 0
    Pit 4 - Mia 4
    Chi 2 - Mia 3'''
    assert(getRecord('Pit', scores) == (1, 2, 1))
    assert(getRecord('Mia', scores) == (2, 0, 1))
    assert(getRecord('Chi', scores) == (1, 2, 0))
    assert(getRecord('Det', scores) == (0, 0, 0))
    print('Passed')

def testPersonClass():
    print('Testing Person Class...', end='')
    fred = Person('fred', 32)
    # Note that fred != "fred" - one is an object, and the other is a string.
    assert(isinstance(fred, Person))
    assert(fred.getName() == 'fred')
    assert(fred.getAge() == 32)
    # Note: person.getFriends() returns a list of Person objects who
    #       are the friends of this person, listed in the order that
    #       they were added.
    # Note: person.getFriendNames() returns a list of strings, the
    #       names of the friends of this person.  This list is sorted!
    assert(fred.getFriends() == [ ])
    assert(fred.getFriendsNames() == [ ])

    wilma = Person('wilma', 35)
    assert(wilma.getName() == 'wilma')
    assert(wilma.getAge() == 35)
    assert(wilma.getFriends() == [ ])

    wilma.addFriend(fred)
    assert(wilma.getFriends() == [fred])
    print(wilma.getFriendsNames())
    assert(wilma.getFriendsNames() == ['fred'])
    assert(fred.getFriends() == [wilma]) # friends are mutual!
    assert(fred.getFriendsNames() == ['wilma'])

    wilma.addFriend(fred)
    assert(wilma.getFriends() == [fred]) # don't add twice!

    betty = Person('betty', 29)
    fred.addFriend(betty)
    assert(fred.getFriendsNames() == ['betty', 'wilma'])

    pebbles = Person('pebbles', 4)
    betty.addFriend(pebbles)
    assert(betty.getFriendsNames() == ['fred', 'pebbles'])

    barney = Person('barney', 28)
    barney.addFriend(pebbles)
    barney.addFriend(betty)
    barney.addFriends(fred) # add ALL of Fred's friends as Barney's friends
    assert(barney.getFriends() == [pebbles, betty, wilma])
    print(barney.getFriendsNames)
    assert(barney.getFriendsNames() == ['betty', 'pebbles', 'wilma'])
    fred.addFriend(wilma)
    fred.addFriend(barney)
    assert(fred.getFriends() == [wilma, betty, barney])
    assert(fred.getFriendsNames() == ['barney', 'betty', 'wilma']) # sorted!
    assert(barney.getFriends() == [pebbles, betty, wilma, fred])
    assert(barney.getFriendsNames() == ['betty', 'fred', 'pebbles', 'wilma'])
    print('Passed!')

def testGetPairSum():
    print("Testing getPairSum()...", end="")
    assert(getPairSum([1], 1) == None)
    assert(getPairSum([5, 2], 7) in [ (5, 2), (2, 5) ])
    assert(getPairSum([10, -1, 1, -8, 3, 1], 2) in
                      [ (10, -8), (-8, 10),(-1, 3), (3, -1), (1, 1) ])
    assert(getPairSum([10, -1, 1, -8, 3, 1], 10) == None)
    assert(getPairSum([10, -1, 1, -8, 3, 1, 8, 19, 0, 5], 10) in
                      [ (10, 0), (0, 10)] )
    assert(getPairSum([10, -1, 1, -8, 3, 1, 8, 19, -9, 5], 10) in
                      [ (19, -9), (-9, 19)] )
    assert(getPairSum([1, 4, 3], 2) == None) # catches reusing values! 1+1...
    assert(getPairSum([5, 5], 10)==(5, 5))
    print("Passed!")

def testContainsPythagoreanTriple():
    print("Testing containsPythagoreanTriple()...", end="")
    assert(containsPythagoreanTriple([1,3,6,2,5,1,4]) == True)
    assert(containsPythagoreanTriple([1,3,6,2,8,1,4]) == False)
    assert(containsPythagoreanTriple([1,730,3,6,54,2,8,1,728,4])
                                      == True) # 54, 728, 730
    assert(containsPythagoreanTriple([1,730,3,6,54,2,8,1,729,4]) == False)
    assert(containsPythagoreanTriple([1,731,3,6,54,2,8,1,728,4]) == False)
    assert(containsPythagoreanTriple([1,731,3,6,54,2,8,1,728,4,
                                6253, 7800, 9997]) == True) # 6253, 7800, 9997
    assert(containsPythagoreanTriple([1,731,3,6,54,2,8,1,728,4,
                                      6253, 7800, 9998]) == False)
    assert(containsPythagoreanTriple([1,731,3,6,54,2,8,1,728,4,
                                      6253, 7800, 9996]) == False)
    assert(containsPythagoreanTriple([1, 2, 3, 67, 65, 35,83, 72, 
                                      97, 25, 98, 12]) == True) # 65, 72, 97
    assert(containsPythagoreanTriple([1, 1, 1]) == False)
    assert(containsPythagoreanTriple([1, 1, 2]) == False)
    assert(containsPythagoreanTriple([3, 5, 5]) == False)
    print("Passed!")

def testMovieAwards():
    print('Testing movieAwards()...', end='')
    tests = [
      (({ ("Best Picture", "The Shape of Water"), 
          ("Best Actor", "Darkest Hour"),
          ("Best Actress", "Three Billboards Outside Ebbing, Missouri"),
          ("Best Director", "The Shape of Water") },),
        { "Darkest Hour" : 1,
          "Three Billboards Outside Ebbing, Missouri" : 1,
          "The Shape of Water" : 2 }),
      (({ ("Best Picture", "Moonlight"),
          ("Best Director", "La La Land"),
          ("Best Actor", "Manchester by the Sea"),
          ("Best Actress", "La La Land") },),
        { "Moonlight" : 1,
          "La La Land" : 2,
          "Manchester by the Sea" : 1 }),
      (({ ("Best Picture", "12 Years a Slave"),
          ("Best Director", "Gravity"),
          ("Best Actor", "Dallas Buyers Club"),
          ("Best Actress", "Blue Jasmine") },),
        { "12 Years a Slave" : 1,
          "Gravity" : 1,
          "Dallas Buyers Club" : 1,
          "Blue Jasmine" : 1 }),
      (({ ("Best Picture", "The King's Speech"),
          ("Best Director", "The King's Speech"),
          ("Best Actor", "The King's Speech") },),
        { "The King's Speech" : 3}),
      (({ ("Best Picture", "Spotlight"), ("Best Director", "The Revenant"),
          ("Best Actor", "The Revenant"), ("Best Actress", "Room"),
          ("Best Supporting Actor", "Bridge of Spies"),
          ("Best Supporting Actress", "The Danish Girl"),
          ("Best Original Screenplay", "Spotlight"),
          ("Best Adapted Screenplay", "The Big Short"),
          ("Best Production Design", "Mad Max: Fury Road"),
          ("Best Cinematography", "The Revenant") },),
        { "Spotlight" : 2,
          "The Revenant" : 3,
          "Room" : 1,
          "Bridge of Spies" : 1,
          "The Danish Girl" : 1,
          "The Big Short" : 1,
          "Mad Max: Fury Road" : 1 }),
       ((set(),), { }),
            ]
    for args,result in tests:
        if (movieAwards(*args) != result):
            print('movieAwards failed:')
            print(args)
            print(result)
            assert(False)
    print('Passed!')

def testFriendsOfFriends():
    print("Testing friendsOfFriends()...", end="")
    d = dict()
    d["fred"] = set(["wilma", "betty", "barney", "bam-bam"])
    d["wilma"] = set(["fred", "betty", "dino"])
    d["betty"] = d["barney"] = d["bam-bam"] = d["dino"] = set()
    fof = friendsOfFriends(d)
    assert(fof["fred"] == set(["dino"]))
    assert(fof["wilma"] == set(["barney", "bam-bam"]))
    result = { "fred":set(["dino"]),
               "wilma":set(["barney", "bam-bam"]),
               "betty":set(),
               "barney":set(),
               "dino":set(),
               "bam-bam":set()
             }
    assert(fof == result)
    d = dict()
    #                A    B    C    D     E     F
    d["A"]  = set([      "B",      "D",        "F" ])
    d["B"]  = set([ "A",      "C", "D",  "E",      ])
    d["C"]  = set([                                ])
    d["D"]  = set([      "B",            "E",  "F" ])
    d["E"]  = set([           "C", "D"             ])
    d["F"]  = set([                "D"             ])
    fof = friendsOfFriends(d)
    assert(fof["A"] == set(["C", "E"]))
    assert(fof["B"] == set(["F"]))
    assert(fof["C"] == set([]))
    assert(fof["D"] == set(["A", "C"]))
    assert(fof["E"] == set(["B", "F"]))
    assert(fof["F"] == set(["B", "E"]))
    result = { "A":set(["C", "E"]),
               "B":set(["F"]),
               "C":set([]),
               "D":set(["A", "C"]),
               "E":set(["B", "F"]),
               "F":set(["B", "E"])
              }
    assert(fof == result)
    print("Passed!")

def testBonusAnimation():
    print('Note: You must visually inspect your bonus animation to test it.')
    bonusAnimation()

def testAll():
    testNearestPreSquareNumber()
    testGetRecord()
    testPersonClass()
    testGetPairSum()
    testContainsPythagoreanTriple()
    testMovieAwards()
    testFriendsOfFriends()
    # testBonusAnimation()

#################################################
# main
#################################################

def main():
    cs112_s22_week8_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
