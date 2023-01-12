#################################################
# hw2.py
# name: alanis zhao
# andrew id: aazhao
# section: q
#################################################

import cs112_s22_week2_linter
import math
import random

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

def digitCount(n): #counts number of digits
    n=abs(n)
    if (n==0):
        return 1
    x=0
    while (n>0):
        x+=1
        n//=10
    return x

def gcd(a,b): #finds gcd of two pos ints
    while (b>0):
        last=a
        a=b
        b=last%b
    return a

def hasConsecutiveDigits(n): #returns if an int has 2+ consec digits
    if (type(n)!=int):
        return False
    n=abs(n)
    while (n>0):
        first=n%10
        mid=(n-first)//10
        second=mid%10
        if (first==second):
            return True
        n//=10
    return False

def sumDigits(n): #returns sum of digits of int
    n=abs(n)
    added=0
    while (n>0):
        n1=n%10
        n//=10
        added+=n1
    return added

def isPrime(n): #returns if int is prime
    if (n<2):
        return False
    for factor in range(2,n):
        if (n%factor==0):
            return False
    return True
    
def isAddPrime(n): #returns if sum of digs and num is prime
    return (isPrime(sumDigits(n)) and isPrime(n))

def nthAdditivePrime(n): # finds nth additive prime
    n1=0
    n2=0
    while (n1<=n):
        n2+=1
        if (isAddPrime(n2)):
            n1+=1
    return n2

def howManyTimes(number, n): #how many times number is in int
    num=0
    count=0
    while (n>0):
        num=n%10
        if (num==number):
            count+=1
        n//=10
    return count

def mostFrequentDigit(n): #finds most freq dig of number
    n=abs(n)
    currMost=0
    currDig=0
    for x in range(0,10):
        if (howManyTimes(x,n) > currMost):
            currMost=howManyTimes(x,n)
            currDig=x
    return currDig

def numDigits(n): #finds num digits of int
    num=0
    if (n==0):
        return 1
    while (n>0):
        n//=10
        num+=1
    return num

def rotate(n): #rotates an int
    end=n%10
    n//=10
    power=10**int(numDigits(n))
    x=end*power
    return end*power+n

def isRotation(x, y): #sees if two nums r rotations of each other
    if (x==y):
        return True
    digits=numDigits(x)
    num=x
    for p in range (0,digits-1):
        curr=rotate(num)
        if(curr==y):
            return True
        num=curr
        p+=1
    return False

def integral(f, a, b, N): #integral of fxn from a to b w n inter
    sum=0.0
    floated=float(N)
    width=(b-a)/floated
    first=f(a)
    second=f(a+width)
    end=a+width
    for x in range(0, N):
        avg=(first+second)/2
        added=width*(avg)
        sum+=added
        first=second
        end+=width
        second=f(end)
        x+=1
    return sum

#################################################
# Part B
#################################################
def midpoint(x, y):#finds midpt between x and y, y>x
    if (x>=0 and y>0):
        return x+(y-x)/2
    elif (x<0 and y>0):
        return x+(y-x)/2
    else:
        return x+(abs(x)-abs(y))/2

def findZeroWithBisection(f, x0, x1, epsilon): #finds 0 of fxn
    curr=midpoint(x1,x0)
    lower=x0
    higher=x1
    if (f(x1)*f(x0)>0):
        return None
    while (almostEqual(higher-lower, epsilon) != True):
        if (almostEqual(f(curr),0)):
            return curr
        elif (f(lower)*f(curr)>0):
            lower=curr
            curr=midpoint(lower, higher)
        else:
            higher=curr
            curr=midpoint(lower, higher)
    return curr

def carrylessAdd(x1, x2): #adds 2 ints w/o carrying
    returned=0
    dig=0
    if (x1>x2):
        dig=numDigits(x1)
    else:
        dig=numDigits(x2)
    for x in range (0,dig):
        end1=x1%10
        end2=x2%10
        added=(end1 + end2)%10
        returned+=added*(10**x)
        x1//=10
        x2//=10
        x+=1
    return returned

def sumOfPrimes(n): #sum of digits prime factors
    added=0
    num=n
    curr=2
    while (curr<=num):
        if (isPrime(curr) and num%curr==0):
            added+=sumDigits(curr)
            num//=curr
            pass
        else:
            curr+=1
    return added

def isSmith(n): #sum of digits = sum of prime factors
    if(isPrime(n)):
        return False
    sumDigs=sumDigits(n)
    sumPrimes=sumOfPrimes(n)
    if (sumDigs==sumPrimes):
        return True
    else:
        return False

def nthSmithNumber(n): #returns nth smith number
    if(n==0):
        return 4
    count=0
    currNum=5
    while (count<n):
        if(isSmith(currNum)):
            count+=1
        currNum+=1
    return currNum-1

def playPig(): #pig game, fxn is long due to prompts
    sum1=0
    sum2=0
    turn=1
    print('Starting Game:')
    print('Current Player 1 Score: '+ str(sum1))
    print('Current Player 2 Score: '+ str(sum2))
    while(sum1<=100 and sum2<=100):
        while(turn%2==1):
            print('Player 1 Turn')
            roll1=random.randint(1,6)
            print('Your roll is: '+ str(roll1))
            if(roll1==1):
                print('You have lost your turn')
                turn+=1
                break
            else:
                sum1+=roll1
                print('Your sum is now: '+ str(sum1))
                if(sum1 >=100):
                    print('Player 1 has won')
                    break
            resp1=input('Enter continue to keep' +
                        'going or quit to end your turn:')
            if(resp1=='continue'):
                pass
            else:
                turn+=1
        while(turn%2==0):
            print('Player 2 Turn')
            roll2=random.randint(1,6)
            print('Your roll is: '+ str(roll2))
            if(roll2==1):
                print('You have lost your turn')
                turn+=1
                break
            else:
                sum2+=roll2
                print('Your sum is now: '+ str(sum2))
                if(sum2 >=100):
                    print('Player 2 has won')
                    break
            resp2 = input('Enter continue to keep' +  
                            ' going or quit to end your turn:')
            if(resp2=='continue'):
                pass
            else:
                turn+=1

#################################################
# Bonus/Optional
#################################################

def bonusPlay112(game):
    return 42

def bonusCarrylessMultiply(x1, x2):
    return 42

############################
# spicy bonus: integerDataStructures
############################

def intCat(n, m): pass
def lengthEncode(value): pass
def lengthDecode(encoding): pass
def lengthDecodeLeftmostValue(encoding): pass
def newIntList(): pass
def intListLen(intList): pass
def intListGet(intList, i): pass
def intListSet(intList, i, value): pass
def intListAppend(intList, value): pass
def intListPop(intList): pass
def newIntSet(): pass
def intSetAdd(intSet, value): pass
def intSetContains(intSet, value): pass
def newIntMap(): pass
def intMapGet(intMap, key): pass
def intMapContains(intMap,key): pass
def intMapSet(intMap, key, value): pass
def newIntFSM(): pass
def isAcceptingState(fsm, state): pass
def addAcceptingState(fsm, state): pass
def setTransition(fsm, fromState, digit, toState): pass
def getTransition(fsm, fromState, digit): pass
def accepts(fsm, inputValue): pass
def states(fsm, inputValue): pass
def encodeString(s): pass
def decodeString(intList): pass

#################################################
# Test Functions
#################################################

def testDigitCount():
    print('Testing digitCount()...', end='')
    assert(digitCount(3) == 1)
    assert(digitCount(33) == 2)
    assert(digitCount(3030) == 4)
    assert(digitCount(-3030) == 4)
    assert(digitCount(0) == 1)
    print('Passed!')

def testGcd():
    print('Testing gcd()...', end='')
    assert(gcd(3, 3) == 3)
    assert(gcd(3**6, 3**6) == 3**6)
    assert(gcd(3**6, 2**6) == 1)
    assert (gcd(2*3*4*5,3*5) == 15)
    x = 1568160 # 2**5 * 3**4 * 5**1 *        11**2
    y = 3143448 # 2**3 * 3**6 *        7**2 * 11**1
    g =    7128 # 2**3 * 3**4 *               11**1
    assert(gcd(x, y) == g)
    print('Passed!')

def testHasConsecutiveDigits():
    print('Testing hasConsecutiveDigits()...', end='')
    assert(hasConsecutiveDigits(0) == False)
    assert(hasConsecutiveDigits(123456789) == False)
    assert(hasConsecutiveDigits(1212) == False)
    assert(hasConsecutiveDigits(1212111212) == True)
    assert(hasConsecutiveDigits(33) == True)
    assert(hasConsecutiveDigits(-1212111212) == True)
    print('Passed!')

def testNthAdditivePrime():
    print('Testing nthAdditivePrime()... ', end='')
    assert(nthAdditivePrime(0) == 2)
    assert(nthAdditivePrime(1) == 3)
    assert(nthAdditivePrime(5) == 23)
    assert(nthAdditivePrime(10) == 61)
    assert(nthAdditivePrime(15) == 113)
    print('Passed!')

def testMostFrequentDigit():
    print('Testing mostFrequentDigit()...', end='')
    assert mostFrequentDigit(0) == 0
    assert mostFrequentDigit(1223) == 2
    assert mostFrequentDigit(-12233) == 2
    assert mostFrequentDigit(1223322332) == 2
    assert mostFrequentDigit(123456789) == 1
    assert mostFrequentDigit(1234567789) == 7
    assert mostFrequentDigit(1000123456789) == 0
    print('Passed!')

def testIsRotation():
    print('Testing isRotation()... ', end='')
    assert(isRotation(1, 1) == True)
    assert(isRotation(1234, 4123) == True)
    assert(isRotation(1234, 3412) == True)
    assert(isRotation(1234, 2341) == True)
    assert(isRotation(1234, 1234) == True)
    assert(isRotation(1234, 123) == False)
    assert(isRotation(1234, 12345) == False)
    assert(isRotation(1234, 1235) == False)
    assert(isRotation(1234, 1243) == False)
    assert(isRotation(12345, 45123) == True)
    print('Passed!')

def f1(x): return 42.0
def i1(x): return 42.0*x 
def f2(x): return 2.0*x  + 1
def i2(x): return x**2.0 + x
def f3(x): return 9.0*x**2.0
def i3(x): return 3.0*x**3.0
def f4(x): return math.cos(x)
def i4(x): return math.sin(x)


def testIntegral():
    print('Testing integral()...', end='')
    epsilon = 10**-4
    assert(almostEqual(integral(f1, -5.0, +5.0, 1), (i1(+5.0)-i1(-5.0)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f1, -5.0, +5.0, 10), (i1(+5)-i1(-5.0)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1.0, 2.0, 1), 4.0,
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1.0, 2.0, 250), (i2(2.0)-i2(1.0)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f3, 4.0, 5.0, 250), (i3(5.0)-i3(4.0)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f4, 1.0, 2.0, 250), (i4(2.0)-i4(1.0)),
                      epsilon=epsilon))
    print("Passed!")

def testFindZeroWithBisection():
    print('Testing findZeroWithBisection()... ', end='')
    def f1(x): return x*x - 2 # root at x=sqrt(2)
    x = findZeroWithBisection(f1, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.41421356192))   
    def f2(x): return x**2 - (x + 1)  # root at x=phi
    x = findZeroWithBisection(f2, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.61803398887))
    def f3(x): return x**5 - 2**x # f(1)<0, f(2)>0
    x = findZeroWithBisection(f3, 1, 2, 0.000000001)
    assert(almostEqual(x, 1.17727855081))
    print('Passed!')

def testCarrylessAdd():
    print('Testing carrylessAdd()... ', end='')
    assert(carrylessAdd(785, 376) == 51)
    assert(carrylessAdd(0, 376) == 376)
    assert(carrylessAdd(785, 0) == 785)
    assert(carrylessAdd(30, 376) == 306)
    assert(carrylessAdd(785, 30) == 715)
    assert(carrylessAdd(12345678900, 38984034003) == 40229602903)
    print('Passed!')

def testNthSmithNumber():
    print('Testing nthSmithNumber()... ', end='')
    assert(nthSmithNumber(0) == 4)
    assert(nthSmithNumber(1) == 22)
    assert(nthSmithNumber(2) == 27)
    assert(nthSmithNumber(3) == 58)
    assert(nthSmithNumber(4) == 85)
    assert(nthSmithNumber(5) == 94)
    print('Passed!')

def testPlayPig():
    print('** Note: You need to manually test playPig()')

def testBonusPlay112():
    print("Testing bonusPlay112()... ", end="")
    assert(bonusPlay112( 5 ) == "88888: Unfinished!")
    assert(bonusPlay112( 521 ) == "81888: Unfinished!")
    assert(bonusPlay112( 52112 ) == "21888: Unfinished!")
    assert(bonusPlay112( 5211231 ) == "21188: Unfinished!")
    assert(bonusPlay112( 521123142 ) == "21128: Player 2 wins!")
    assert(bonusPlay112( 521123151 ) == "21181: Unfinished!")
    assert(bonusPlay112( 52112315142 ) == "21121: Player 1 wins!")
    assert(bonusPlay112( 523 ) == "88888: Player 1: move must be 1 or 2!")
    assert(bonusPlay112( 51223 ) == "28888: Player 2: move must be 1 or 2!")
    assert(bonusPlay112( 51211 ) == "28888: Player 2: occupied!")
    assert(bonusPlay112( 5122221 ) == "22888: Player 1: occupied!")
    assert(bonusPlay112( 51261 ) == "28888: Player 2: offboard!")
    assert(bonusPlay112( 51122324152 ) == "12212: Tie!")
    print("Passed!")

def testBonusCarrylessMultiply():
    print("Testing bonusCarrylessMultiply()...", end="")
    assert(bonusCarrylessMultiply(643, 59) == 417)
    assert(bonusCarrylessMultiply(6412, 387) == 807234)
    print("Passed!")

# Integer Data Structures

def testLengthEncode():
    print('Testing lengthEncode()...', end='')
    assert(lengthEncode(789) == 113789)
    assert(lengthEncode(-789) == 213789)
    assert(lengthEncode(1234512345) == 12101234512345)
    assert(lengthEncode(-1234512345) == 22101234512345)
    assert(lengthEncode(0) == 1110)
    print('Passed!')

def testLengthDecodeLeftmostValue():
    print('Testing lengthDecodeLeftmostValue()...', end='')
    assert(lengthDecodeLeftmostValue(111211131114) == (2, 11131114))
    assert(lengthDecodeLeftmostValue(112341115) == (34, 1115))
    assert(lengthDecodeLeftmostValue(111211101110) == (2, 11101110))
    assert(lengthDecodeLeftmostValue(11101110) == (0, 1110))
    print('Passed!')

def testLengthDecode():
    print('Testing lengthDecode()...', end='')
    assert(lengthDecode(113789) == 789)
    assert(lengthDecode(213789) == -789)
    assert(lengthDecode(12101234512345) == 1234512345)
    assert(lengthDecode(22101234512345) == -1234512345)
    assert(lengthDecode(1110) == 0)
    print('Passed!')

def testIntList():
    print('Testing intList functions...', end='')
    a1 = newIntList()
    assert(a1 == 1110) # length = 0, list = []
    assert(intListLen(a1) == 0)
    assert(intListGet(a1, 0) == 'index out of range')

    a1 = intListAppend(a1, 42)
    assert(a1 == 111111242) # length = 1, list = [42]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 42)
    assert(intListGet(a1, 1) == 'index out of range')
    assert(intListSet(a1, 1, 99) == 'index out of range')

    a1 = intListSet(a1, 0, 567)
    assert(a1 == 1111113567) # length = 1, list = [567]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 567)

    a1 = intListAppend(a1, 8888)
    a1 = intListSet(a1, 0, 9)
    assert(a1 == 111211191148888) # length = 2, list = [9, 8888]
    assert(intListLen(a1) == 2)
    assert(intListGet(a1, 0) == 9)
    assert(intListGet(a1, 1) == 8888)

    a1, poppedValue = intListPop(a1)
    assert(poppedValue == 8888)
    assert(a1 == 11111119) # length = 1, list = [9]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 9)
    assert(intListGet(a1, 1) == 'index out of range')

    a2 = newIntList()
    a2 = intListAppend(a2, 0)
    assert(a2 == 11111110)
    a2 = intListAppend(a2, 0)
    assert(a2 == 111211101110)
    print('Passed!')

def testIntSet():
    print('Testing intSet functions...', end='')
    s = newIntSet()
    assert(s == 1110) # length = 0
    assert(intSetContains(s, 42) == False)
    s = intSetAdd(s, 42)
    assert(s == 111111242) # length = 1, set = [42]
    assert(intSetContains(s, 42) == True)
    s = intSetAdd(s, 42) # multiple adds --> still just one
    assert(s == 111111242) # length = 1, set = [42]
    assert(intSetContains(s, 42) == True)
    print('Passed!')

def testIntMap():
    print('Testing intMap functions...', end='')
    m = newIntMap()
    assert(m == 1110) # length = 0
    assert(intMapContains(m, 42) == False)
    assert(intMapGet(m, 42) == 'no such key')
    m = intMapSet(m, 42, 73)
    assert(m == 11121124211273) # length = 2, map = [42, 73]
    assert(intMapContains(m, 42) == True)
    assert(intMapGet(m, 42) == 73)
    m = intMapSet(m, 42, 98765)
    assert(m == 11121124211598765) # length = 2, map = [42, 98765]
    assert(intMapGet(m, 42) == 98765)
    m = intMapSet(m, 99, 0)
    assert(m == 11141124211598765112991110) # length = 4, 
                                            # map = [42, 98765, 99, 0]
    assert(intMapGet(m, 42) == 98765)
    assert(intMapGet(m, 99) == 0)
    print('Passed!')

def testIntFSM():
    print('Testing intFSM functions...', end='')
    fsm = newIntFSM()
    assert(fsm == 111211411101141110) # length = 2, 
                                      # [empty stateMap, empty startStateSet]
    assert(isAcceptingState(fsm, 1) == False)

    fsm = addAcceptingState(fsm, 1)
    assert(fsm == 1112114111011811111111)
    assert(isAcceptingState(fsm, 1) == True)

    assert(getTransition(fsm, 0, 8) == 'no such transition')
    fsm = setTransition(fsm, 4, 5, 6)
    # map[5] = 6: 111211151116
    # map[4] = (map[5] = 6):  111211141212111211151116
    assert(fsm == 1112122411121114121211121115111611811111111)
    assert(getTransition(fsm, 4, 5) == 6)

    fsm = setTransition(fsm, 4, 7, 8)
    fsm = setTransition(fsm, 5, 7, 9)
    assert(getTransition(fsm, 4, 5) == 6)
    assert(getTransition(fsm, 4, 7) == 8)
    assert(getTransition(fsm, 5, 7) == 9)

    fsm = newIntFSM()
    assert(fsm == 111211411101141110) # length = 2, 
                                      # [empty stateMap, empty startStateSet]
    fsm = setTransition(fsm, 0, 5, 6)
    # map[5] = 6: 111211151116
    # map[0] = (map[5] = 6):  111211101212111211151116
    assert(fsm == 111212241112111012121112111511161141110)
    assert(getTransition(fsm, 0, 5) == 6)

    print('Passed!')

def testAccepts():
    print('Testing accepts()...', end='')
    fsm = newIntFSM()
    # fsm accepts 6*7+8
    fsm = addAcceptingState(fsm, 3)
    fsm = setTransition(fsm, 1, 6, 1) # At state 1, receive 6, move to state 1
    fsm = setTransition(fsm, 1, 7, 2) # At state 1, receive 7, move to state 2
    fsm = setTransition(fsm, 2, 7, 2) # At state 1, receive 7, move to state 2
    fsm = setTransition(fsm, 2, 8, 3) # At state 1, receive 8, move to state 3
    assert(accepts(fsm, 78) == True)
    assert(states(fsm, 78) == 1113111111121113) # length = 3, list = [1,2,3]
    assert(accepts(fsm, 678) == True)
    assert(states(fsm, 678) == 11141111111111121113) # length = 4, 
                                                     # list = [1,1,2,3]

    assert(accepts(fsm, 5) == False)
    assert(accepts(fsm, 788) == False)
    assert(accepts(fsm, 67) == False)
    assert(accepts(fsm, 666678) == True)
    assert(accepts(fsm, 66667777777777778) == True)
    assert(accepts(fsm, 7777777777778) == True)
    assert(accepts(fsm, 666677777777777788) == False)
    assert(accepts(fsm, 77777777777788) == False)
    assert(accepts(fsm, 7777777777778) == True)
    assert(accepts(fsm, 67777777777778) == True)
    print('Passed!')

def testEncodeDecodeStrings():
    print('Testing encodeString and decodeString...', end='')
    assert(encodeString('A') == 111111265) # length = 1, str = [65]
    assert(encodeString('f') == 1111113102) # length = 1, str = [102]
    assert(encodeString('3') == 111111251) # length = 1, str = [51]
    assert(encodeString('!') == 111111233) # length = 1, str = [33]
    assert(encodeString('Af3!') == 1114112651131021125111233) # length = 4, 
                                                          # str = [65,102,51,33]
    assert(decodeString(111111265) == 'A')
    assert(decodeString(1114112651131021125111233) == 'Af3!')
    assert(decodeString(encodeString('WOW!!!')) == 'WOW!!!')
    print('Passed!')

def testIntegerDataStructures():
    testLengthEncode()
    testLengthDecode()
    testLengthDecodeLeftmostValue()
    testIntList()
    testIntSet()
    testIntMap()
    testIntFSM()
    testAccepts()
    testEncodeDecodeStrings()

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # Part A:
    testDigitCount()
    testGcd()   
    testHasConsecutiveDigits()   
    testNthAdditivePrime()   
    testMostFrequentDigit()
    testIsRotation()
    testIntegral()

    # Part B:
    testFindZeroWithBisection()
    testCarrylessAdd()
    testNthSmithNumber()
    testPlayPig()

    # Bonus:
    # testBonusPlay112()
    # testBonusCarrylessMultiply()
    # testIntegerDataStructures()

def main():
    cs112_s22_week2_linter.lint()
    testAll()
    playPig()

if __name__ == '__main__':
    main()
