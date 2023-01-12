#################################################
# hw1.py
# name: Alanis Zhao
# andrew id: aazhao
#################################################

import cs112_s22_week1_linter
import math

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

#################################################
# Part A
#################################################

def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def circlesIntersect(x1, y1, r1, x2, y2, r2):
    dis = distance(x1, y1, x2, y2)
    if (dis <= (r1+r2)):
        return True
    else:
        return False

def getInRange(x, bound1, bound2):
    if bound1 <= x <= bound2 or bound2 <= x <= bound1:
        return x
    elif x <= bound1 <= bound2 or bound2 <= bound1 <= x:
        return bound1
    elif x <= bound2 <= bound1 or bound1 <= bound2 <= x:
        return bound2

def eggCartons(eggs):
    num = eggs//12
    if eggs%12 == 0:
        return num
    else:
        return num + 1

def pascalsTriangleValue(row, col):
    if (type(row) != int or type(col) != int):
        return None
    elif (row < 0 or col < 0 or col > row): 
        return None
    else:
        return roundHalfUp(math.factorial(row)/
        (math.factorial(col)*math.factorial(row-col)))

def getKthDigit(n, k):
    powerNum = 10**k
    changedNum = (abs(n))//powerNum
    return changedNum%10
#Write the function setKthDigit(n, k, d) that takes three integers
#  -- n, k, and d -- where n is a possibly-negative int, 
# k is a non-negative int, and d is a non-negative single digit
#  (between 0 and 9 inclusive). This function returns the number
#  n with the kth digit replaced with d. 
def setKthDigit(n, k, d):
    if n>=0:
        num = n
        powerNum = 10**k #numer it is div by to have the kth digit at the end
        changedNum = num//powerNum # num w k digit at end
        end = num - changedNum*powerNum #part that needs to be added
        beg = changedNum - getKthDigit(n,k) + d
        return beg*powerNum + end
    else:
        num = abs(n)
        powerNum = 10**k #numer it is div by to have the kth digit at the end
        changedNum = num//powerNum # num w k digit at end
        end = num - changedNum*powerNum #part that needs to be added
        beg = changedNum - getKthDigit(n,k) + d
        return (beg*powerNum + end)*(-1)
    

#################################################
# Part B
#################################################

#Write the function nearestOdd(n) that takes an int or float n, and returns as
#  an int value the nearest odd number to n. In the case of a tie, return the
#  smaller odd value. Note that the result must be an int, so nearestOdd(13.0)
#  is the int 13, and not the float 13.0.
        
def nearestOdd(n):
    if (type(n)==int):
        if (n%2==0):
            return n-1
        else:
            return n
    else :
        num = roundHalfUp(n)
        roundError = float(num)-n
        if (num%2==0):
            if (roundError < 0):
                return num+1
            else: 
                return num-1
        else:
            return num

#14.3 14.7 15.3 15.7 12.001

def numberOfPoolBalls(rows):
    rows1 = rows + 1
    return rows*rows1/2

def numberOfPoolBallRows(balls):
    numBalls = float(balls)
    var1 = math.sqrt(1+8*numBalls) - 1
    rows = var1/2
    intRows = int(rows)
    if (rows==float(intRows)):
        return intRows
    else: 
        return intRows + 1

def colorBlender(rgb1, rgb2, midpoints, n):
    if (n>midpoints+1 or n < 0):
        return None
    elif (n==0):
        return rgb1
    elif (n==midpoints+1 or rgb1==rgb2):
        return rgb2

    int11 = int(float(rgb1)/1000000)
    int12 = int(float((rgb1-int11*1000000)/1000))
    int13 = int(rgb1-int11*1000000-int12*1000)

    int21 = int(float(rgb2)/1000000)
    int22 = int(float((rgb2-int21*1000000)/1000))
    int23 = int(rgb2-int21*1000000-int22*1000)

    div1 = float(abs(int11-int21)/(midpoints+1))
    div2 = float(abs(int12-int22)/(midpoints+1))
    div3 = float(abs(int13-int23)/(midpoints+1))

    #print(int11)
    #print(int12)
    #print(int13)
    #print(int21)
    #print(int22)
    #print(int23)


    ret1=1
    ret2=2
    ret3=3

    if (int11>int21):
        ret1 = int(roundHalfUp(float(int11) - div1*n))
    else:
        ret1 = int(roundHalfUp(float(int11) + div1*n))
    
    if (int12>int22):
        ret2 = int(roundHalfUp(float(int12) - div2*n))
    else:
        ret2 = int(roundHalfUp(float(int12) + div2*n))
    
    if (int13>int23):
        ret3 = int(roundHalfUp(float(int13) - div3*n))
    else:
        ret3 = int(roundHalfUp(float(int13) + div3*n))
    
    #print(ret1)
    #print(ret2)
    #print(ret3)

    final1 = ret1*1000000
    final2 = ret2*1000
    final3 = ret3

    #print(final1)
    #print(final2)
    #print(final3)

    #print (final1 + final2 + final3)
    return (final1 + final2 + final3)


    





#################################################
# Bonus/Optional
#################################################

def bonusPlayThreeDiceYahtzee(dice):
    return 42

def bonusFindIntRootsOfCubic(a, b, c, d):
    return 42

#################################################
# Test Functions
#################################################

def testDistance():
    print('Testing distance()... ', end='')
    assert(almostEqual(distance(0, 0, 3, 4), 5))
    assert(almostEqual(distance(-1, -2, 3, 1), 5))
    assert(almostEqual(distance(-.5, .5, .5, -.5), 2**0.5))
    print('Passed!')

def testCirclesIntersect():
    print('Testing circlesIntersect()... ', end='')
    assert(circlesIntersect(0, 0, 2, 3, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 4, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 5, 0, 2) == False)
    assert(circlesIntersect(3, 3, 3, 3, -3, 3) == True)
    assert(circlesIntersect(3, 3, 3, 3,- 3, 2.99) == False)
    print('Passed!')

def testGetInRange():
    print('Testing getInRange()... ', end='')
    assert(getInRange(5, 1, 10) == 5)
    assert(getInRange(5, 5, 10) == 5)
    assert(getInRange(5, 9, 10) == 9)
    assert(getInRange(5, 10, 10) == 10)
    assert(getInRange(5, 10, 1) == 5)
    assert(getInRange(5, 10, 5) == 5)
    assert(getInRange(5, 10, 9) == 9)
    assert(getInRange(0, -20, -30) == -20)
    assert(almostEqual(getInRange(0, -20.25, -30.33), -20.25))
    print('Passed!')

def testEggCartons():
    print('Testing eggCartons()... ', end='')
    assert(eggCartons(0) == 0)
    assert(eggCartons(1) == 1)
    assert(eggCartons(12) == 1)
    assert(eggCartons(13) == 2)
    assert(eggCartons(24) == 2)
    assert(eggCartons(25) == 3)
    print('Passed!')

def testPascalsTriangleValue():
    print('Testing pascalsTriangleValue()... ', end='')
    assert(pascalsTriangleValue(3,0) == 1)
    assert(pascalsTriangleValue(3,1) == 3)
    assert(pascalsTriangleValue(3,2) == 3)
    assert(pascalsTriangleValue(3,3) == 1)
    assert(pascalsTriangleValue(1234,0) == 1)
    assert(pascalsTriangleValue(1234,1) == 1234)
    assert(pascalsTriangleValue(1234,2) == 760761)
    assert(pascalsTriangleValue(3,-1) == None)
    assert(pascalsTriangleValue(3,4) == None)
    assert(pascalsTriangleValue(-3,2) == None)
    assert(pascalsTriangleValue('dog', 'cat') == None)
    print('Passed!')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed!')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    print('Passed!')

def testNearestOdd():
    print('Testing nearestOdd()... ', end='')
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    # results must be int's not floats
    assert(isinstance(nearestOdd(13.0), int))
    assert(isinstance(nearestOdd(11.999), int))
    print('Passed!')

def testNumberOfPoolBalls():
    print('Testing numberOfPoolBalls()... ', end='')
    assert(numberOfPoolBalls(0) == 0)
    assert(numberOfPoolBalls(1) == 1)
    assert(numberOfPoolBalls(2) == 3)   # 1+2 == 3
    assert(numberOfPoolBalls(3) == 6)   # 1+2+3 == 6
    assert(numberOfPoolBalls(10) == 55) # 1+2+...+10 == 55
    print('Passed!')

def testNumberOfPoolBallRows():
    print('Testing numberOfPoolBallRows()... ', end='')
    assert(numberOfPoolBallRows(0) == 0)
    assert(numberOfPoolBallRows(1) == 1)
    assert(numberOfPoolBallRows(2) == 2)
    assert(numberOfPoolBallRows(3) == 2)
    assert(numberOfPoolBallRows(4) == 3)
    assert(numberOfPoolBallRows(6) == 3)
    assert(numberOfPoolBallRows(7) == 4)
    assert(numberOfPoolBallRows(10) == 4)
    assert(numberOfPoolBallRows(11) == 5)
    assert(numberOfPoolBallRows(55) == 10)
    assert(numberOfPoolBallRows(56) == 11)
    print('Passed!')

def testColorBlender():
    print('Testing colorBlender()... ', end='')
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    #assert(colorBlender(220020060, 189252201, 3, -1) == None)
    #assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    #assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    #assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    #assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print('Passed!')

def testBonusPlayThreeDiceYahtzee():
    print('Testing bonusPlayThreeDiceYahtzee()...', end='')
    assert(handToDice(123) == (1,2,3))
    assert(handToDice(214) == (2,1,4))
    assert(handToDice(422) == (4,2,2))
    assert(diceToOrderedHand(1,2,3) == 321)
    assert(diceToOrderedHand(6,5,4) == 654)
    assert(diceToOrderedHand(1,4,2) == 421)
    assert(diceToOrderedHand(6,5,6) == 665)
    assert(diceToOrderedHand(2,2,2) == 222)
    assert(playStep2(413, 2312) == (421, 23))
    assert(playStep2(421, 23) == (432, 0))
    assert(playStep2(413, 2345) == (544, 23))
    assert(playStep2(544, 23) == (443, 2))
    assert(playStep2(544, 456) == (644, 45))
    assert(score(432) == 4)
    assert(score(532) == 5)
    assert(score(443) == 10+4+4)
    assert(score(633) == 10+3+3)
    assert(score(333) == 20+3+3+3)
    assert(score(555) == 20+5+5+5)
    assert(bonusPlayThreeDiceYahtzee(2312413) == (432, 4))
    assert(bonusPlayThreeDiceYahtzee(2315413) == (532, 5))
    assert(bonusPlayThreeDiceYahtzee(2345413) == (443, 18))
    assert(bonusPlayThreeDiceYahtzee(2633413) == (633, 16))
    assert(bonusPlayThreeDiceYahtzee(2333413) == (333, 29))
    assert(bonusPlayThreeDiceYahtzee(2333555) == (555, 35))
    print('Passed!')

def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    result1, result2, result3 = bonusFindIntRootsOfCubic(a,b,c,d)
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1+z2+z3)-(m1+m3)
    actual = (m1, m2, m3)
    assert(almostEqual(m1, result1))
    assert(almostEqual(m2, result2))
    assert(almostEqual(m3, result3))

def testBonusFindIntRootsOfCubic():
    print('Testing bonusFindIntRootsOfCubic()...', end='')
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # Part A:
    testDistance()
    testCirclesIntersect()
    testGetInRange()
    testEggCartons()
    testPascalsTriangleValue()
    testGetKthDigit()
    testSetKthDigit()
    # Part B:
    testNearestOdd()
    testNumberOfPoolBalls()
    testNumberOfPoolBallRows()
    testColorBlender()
    # Bonus:
    # testBonusPlayThreeDiceYahtzee()
    # testBonusFindIntRootsOfCubic()

def main():
    cs112_s22_week1_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
