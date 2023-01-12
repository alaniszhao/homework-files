#################################################
# hw4.py
# name: alanis zhao
# andrew id: aazhao
#################################################

import cs112_s22_week4_linter
import math, copy

'''gabi's grade of mine:
-line 72: bad variable name: 'returned' (maybe try 'result')
-doesn't label functions as helper-fn's
-line 112 and 117: efficiency 'for i in range(0,value)' writing 0 is unnecessary

my grade of gabi's
-line 42 - don't use var name sum
-line 242-252 - could use description of what you are returning
-no other comments, she has good comments and variable names, consistent
spacing, uses helper fxns, efficient code :)
'''
#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d): #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def rgbString(red, green, blue):
     return f'#{red:02x}{green:02x}{blue:02x}'

#################################################
# Part A
#################################################

def alternatingSum(L): #adds even indexes, subtracts odd indexes
    result=0
    for i in range(len(L)): #goes through function
        if i%2==0: #if index even
            result+=L[i]
        else: #if index odd
            result-=L[i]
    return result

def median(L): #returns median of list
    srted=sorted(L)
    if (len(L)==0): #returns None for empty list
        return None
    if (len(L)%2==1): #if odd length
        return srted[len(L)//2]
    else: #if even length, avgs two middle values
        upperMiddle=len(L)//2
        result=srted[upperMiddle]+srted[upperMiddle-1]
        return result/2

def smallestDifference(L): #finds smallest abs diff between 2 elems
    if (len(L)<2): #if less than 2 elems
        return -1
    currSmallest=abs(abs(L[0])-abs(L[1])) #sets diff to 1st elem - 2nd elem
    for index1 in range(len(L)): #loops through 1st number
        for index2 in range(len(L)): #loops through second number
            if (index1==index2): #if they're same elem
                continue
            currDiff=abs(L[index1]-L[index2]) #abs diff of 1st and 2nd num
            if (currDiff<currSmallest):
                currSmallest=abs(currDiff)
    return currSmallest

def nondestructiveRemoveRepeats(L): #removes repeated elems non-d
    returned=[]
    for index in range(len(L)): #goes through orig list
        currIndexInRet=False
        for i in returned: #goes through current return list
            if (i==L[index]):
                currIndexInRet=True
        if(currIndexInRet==False):
            returned.append(L[index]) #if not a repeat adds to return list
    return returned

def destructiveRemoveRepeats(L): #removes repeat elems d
    i=0
    while(i<len(L)): #loops through current list
        currNum=L[i]
        index=i+1
        while (index<len(L)): #looks at next element
            if (L[index]==currNum): #removes if it's a repeat
                L.pop(index)
                continue
            index+=1
        i+=1

#################################################
# Part B
#################################################
def removeConsec(L): #removes consecutive equal nums in list
    copiedL=copy.copy(L)
    i=0
    while (i<len(copiedL)-1): #removes l[i+1] if it's same as L[i]
        if (copiedL[i+1]==copiedL[i]):
            copiedL.pop(i+1)
            continue
        i+=1
    return copiedL

def isSorted(L): #tests if fxn is sorted lo/hi or hi/lo, ignores repeats
    nonConsecL=removeConsec(L)
    if(len(nonConsecL)==0 or len(nonConsecL)==1): #if empty or all same num
        return True
    if (nonConsecL[0]<nonConsecL[1]): #low to high test
        for i in range(0,len(nonConsecL)-1):
            if (nonConsecL[i]>=nonConsecL[i+1]):
                return False
        return True
    else: #high to low test
        for i in range(0,len(nonConsecL)-1):
            if (nonConsecL[i]<=nonConsecL[i+1]):
                return False
        return True

def lookAndSay(L): #returns list of lookandsay nums for a list
    if (len(L)==0):return [] #if list is empty
    copiedL=copy.copy(L)
    i=0
    lastNewElem=None
    returned=[]
    while (i<=len(copiedL)-1):#loops through list
        if(i==len(copiedL)-1):#for last element
            if(copiedL[0]!=lastNewElem):#as long as it's not a repeat
                newElem=(1,copiedL[i])
                returned.append(newElem)
                break
        if(copiedL[i]!=copiedL[i+1]):#if not a repeat add it to returned
            newElem=(1,copiedL[i])
            returned.append(newElem)
            i+=1
        else: #works through consec same nums
            count=1
            while(i<len(copiedL)-1): #loops through list
                if(copiedL[i]==copiedL[i+1]): #adds to count if a repeat
                    count+=1
                    copiedL.pop(i+1)
                else: break
            newElem=(count,copiedL[i])
            returned.append(newElem)
            lastNewElem=copiedL[i]
            i+=1
    return returned

def inverseLookAndSay(L):#takes lookandsay number and adds to loop
    returned=[]
    for currT in L: #loops through tuples in L
        count=currT[0]
        num=currT[1]
        for currNum in range(count):#adds the number the correct amt of times
            returned.append(num)
            currNum+=1
    return returned

def multiplyPolynomials(p1, p2): #multiplied coeffs of 2 polynomials
    deg1=len(p1)
    deg2=len(p2)
    endLength=deg1+deg2-1
    returned=[0]*endLength #creates end poly of corr length
    i1=0
    while (i1!=len(p1)): #loops through first poly
        i2=0
        while (i2!=len(p2)): #loops through second poly and multiplies/adds
            currNum=returned[i1+i2]
            multiplied=p1[i1]*p2[i2]
            if(currNum==0):
                returned[i1+i2]=multiplied
            else:
                returned[i1+i2]+=multiplied
            i2+=1
        i1+=1
    return returned

def inList(char, list): #checks if a letter is in a list
    for curr in list: #loops thru list and checks every letter
        if(char==curr):
            return True
    return False

def canMake(word, hand): #checks if you can make a word with a hand
    handC=copy.copy(hand)
    for curr in word: #loops thru list, removes letter if it's in word
        if (inList(curr, handC)):
            handC.remove(curr)
        else:
            return False
    return True

def scoreWord (word, letterS): #returns scrabble score of word
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
           'q','r','s','t','u','v','w','x','y','z']
    score=0
    for curr in word: #loops thru and adds letter score to total
        currIndex=alpha.index(curr)
        score+=letterS[currIndex]
    return score

def bestScrabbleScore(dictionary, letterScores, hand): #finds word w best score
    possWords=[]
    for currWord in dictionary: #creates list of possible words
        if (canMake(currWord,hand)):
            possWords.append(currWord)
    if(len(possWords)==0): #returns none if no words
        return None
    highestScore=0
    wordsAndScores=[]
    for currWord in possWords: #list of tuples with word and it's score
        currScore=scoreWord(currWord,letterScores)
        wordsAndScores.append((currWord,currScore))
        if(currScore>highestScore): #keeps track of highest curr score
            highestScore=currScore
    highestIndexes=[]
    highestWords=[]
    for index in range(len(wordsAndScores)): #list of highest i and words
        currWAS=wordsAndScores[index]
        if(currWAS[1]==highestScore):
            highestIndexes.append(currWAS)
            highestWords.append(currWAS[0])
        index+=1
    if(len(highestIndexes)==1): #returns tuple of word and score
        return (highestWords[0],highestScore)
    else: #returns tuple of list of words and score
        return(highestWords,highestScore)

#################################################
# Bonus/Optional
#################################################

def linearRegression(pointsList):
    return 42

def runSimpleProgram(program, args):
    return 42

#################################################
# Test Functions
#################################################

def _verifyAlternatingSumIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    # ignore result, just checking for destructiveness here
    alternatingSum(a)
    return (a == b)

def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(_verifyAlternatingSumIsNondestructive())
    assert(alternatingSum([ ]) == 0)
    assert(alternatingSum([1]) == 1)
    assert(alternatingSum([1, 5]) == 1-5)
    assert(alternatingSum([1, 5, 17]) == 1-5+17)
    assert(alternatingSum([1, 5, 17, 4]) == 1-5+17-4)
    print('Passed!')

def _verifyMedianIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    # ignore result, just checking for destructiveness here
    median(a)
    return (a == b)

def testMedian():
    print('Testing median()...', end='')
    assert(_verifyMedianIsNondestructive())
    assert(median([ ]) == None)
    assert(median([ 42 ]) == 42)
    assert(almostEqual(median([ 1 ]), 1))
    assert(almostEqual(median([ 1, 2]), 1.5))
    assert(almostEqual(median([ 2, 3, 2, 4, 2]), 2))
    assert(almostEqual(median([ 2, 3, 2, 4, 2, 3]), 2.5))
    # now make sure this is non-destructive
    a = [ 2, 3, 2, 4, 2, 3]
    b = a + [ ]
    assert(almostEqual(median(b), 2.5))
    if (a != b):
        raise Exception('Your median() function should be non-destructive!')
    print('Passed!')

def testSmallestDifference():
    print('Testing smallestDifference()...', end='')
    assert(smallestDifference([]) == -1)
    assert(smallestDifference([2,3,5,9,9]) == 0)
    assert(smallestDifference([-2,-5,7,15]) == 3)
    assert(smallestDifference([19,2,83,6,27]) == 4)
    assert(smallestDifference(list(range(0, 10**3, 5)) + [42]) == 2)
    print('Passed!')

def _verifyNondestructiveRemoveRepeatsIsNondestructive():
    a = [3, 5, 3, 3, 6]
    b = a + [ ] # copy.copy(a)
    # ignore result, just checking for destructiveness here
    nondestructiveRemoveRepeats(a)
    return (a == b)

def testNondestructiveRemoveRepeats():
    print("Testing nondestructiveRemoveRepeats()", end="")
    assert(_verifyNondestructiveRemoveRepeatsIsNondestructive())
    assert(nondestructiveRemoveRepeats([1,3,5,3,3,2,1,7,5]) == [1,3,5,2,7])
    assert(nondestructiveRemoveRepeats([1,2,3,-2]) == [1,2,3,-2])
    print("Passed!")

def testDestructiveRemoveRepeats():
    print("Testing destructiveRemoveRepeats()", end="")
    a = [1,3,5,3,3,2,1,7,5]
    assert(destructiveRemoveRepeats(a) == None)
    assert(a == [1,3,5,2,7])
    b = [1,2,3,-2]
    assert(destructiveRemoveRepeats(b) == None)
    assert(b == [1,2,3,-2])
    print("Passed!")

def testIsSorted():
    print('Testing isSorted()...', end='')
    assert(isSorted([]) == True)
    assert(isSorted([1]) == True)
    assert(isSorted([1,1]) == True)
    assert(isSorted([1,2]) == True)
    assert(isSorted([2,1]) == True)
    assert(isSorted([2,2,2,2,2,1,1,1,1,0]) == True)
    assert(isSorted([1,1,1,1,2,2,2,2,3,3]) == True)
    assert(isSorted([1,2,1]) == False)
    assert(isSorted([1,1,2,1]) == False)
    assert(isSorted(range(10,30,3)) == True)
    assert(isSorted(range(30,10,-3)) == True)
    print('Passed!')

def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = a + [ ] # copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    assert(lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)])
    assert(lookAndSay([2]*5 + [5]*2) == [(5,2), (2,5)])
    assert(lookAndSay([5]*2 + [2]*5) == [(2,5), (5,2)])
    print("Passed!")

def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = a + [ ] # copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    assert(inverseLookAndSay([(5,2), (2,5)]) == [2]*5 + [5]*2)
    assert(inverseLookAndSay([(2,5), (5,2)]) == [5]*2 + [2]*5)
    print("Passed!")

def testMultiplyPolynomials():
    print("Testing multiplyPolynomials()...", end="")
    # (2)*(3) == 6
    assert(multiplyPolynomials([2], [3]) == [6])
    # (2x-4)*(3x+5) == 6x^2 -2x - 20
    assert(multiplyPolynomials([2,-4],[3,5]) == [6,-2,-20])
    # (2x^2-4)*(3x^3+2x) == (6x^5-8x^3-8x)
    assert(multiplyPolynomials([2,0,-4],[3,0,2,0]) == [6,0,-8,0,-8,0])
    print("Passed!")

def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    def dictionary1(): return ["a", "b", "c"]
    def letterScores1(): return [1] * 26
    def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"] 
    def letterScores2(): return [1+(i%5) for i in range(26)]
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("ace")) ==
                                        (["a", "c"], 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("z")) ==
                                        None)
    # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyz")) ==
                                         (["xyz", "zxy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyzy")) ==
                                        (["xyz", "zxy", "yy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")) ==
                                        ("yx", 9))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("yzz")) ==
                                        ("zzy", 7))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("wxz")) ==
                                        None)
    print("Passed!")

def relaxedAlmostEqual(d1, d2):
    epsilon = 10**-3 # really loose here
    return abs(d1 - d2) < epsilon

def tuplesAlmostEqual(t1, t2):
    if (len(t1) != len(t2)): return False
    for i in range(len(t1)):
        if (not relaxedAlmostEqual(t1[i], t2[i])):
            return False
    return True

def testLinearRegression():
    print("Testing bonus problem linearRegression()...", end="")

    ans = linearRegression([(1,3), (2,5), (4,8)])
    target = (1.6429, 1.5, .9972)
    assert(tuplesAlmostEqual(ans, target))
    
    ans = linearRegression([(0,0), (1,2), (3,4)])
    target = ((9.0/7), (2.0/7), .9819805061)
    assert(tuplesAlmostEqual(ans, target))

    #perfect lines
    ans = linearRegression([(1,1), (2,2), (3,3)])
    target = (1.0, 0.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))
    
    ans = linearRegression([(0,1), (-1, -1)])
    target = (2.0, 1.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))

    #horizontal lines
    ans = linearRegression([(1,0), (2,0), (3,0)])
    target = (0.0, 0.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))

    ans = linearRegression([(1,1), (2,1), (-1,1)])
    target = (0.0, 1.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))
    print("Passed!")

def testRunSimpleProgram():
    print("Testing bonus problem runSimpleProgram()...", end="")
    largest = """! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""
    assert(runSimpleProgram(largest, [5, 6]) == 6)
    assert(runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    assert(runSimpleProgram(sumToN, [5]) == 1+2+3+4+5)
    assert(runSimpleProgram(sumToN, [10]) == 10*11//2)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # Part A:
    testAlternatingSum()
    testMedian()
    testSmallestDifference()
    testNondestructiveRemoveRepeats()
    testDestructiveRemoveRepeats()

    # Part B:
    testIsSorted()
    testLookAndSay()
    testInverseLookAndSay()
    testMultiplyPolynomials()
    testBestScrabbleScore()

    # Bonus:
    #testLinearRegression()
    #testRunSimpleProgram() 

def main():
    cs112_s22_week4_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
