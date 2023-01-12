#################################################
# hw3.py
# name: Alanis Zhao
# andrew id: aazhao
#################################################

import cs112_s22_week3_linter
import math
from cmu_112_graphics import *
import re

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

def rotateString(s, k): #rotates s left or right by 1—depends on k
    ret=s
    count=0
    if(k==0): #for efficiency
        return s
    elif(k>0): #rotates left
        while (count<k):
            ret=ret[1:len(s)]+ret[0]
            count+=1
        return ret
    else: #rotates right
        while (count<abs(k)):
            ret=ret[len(s)-1]+ret[0:len(s)-1]
            count+=1
        return ret

def applyCaesarCipher(message, shift): #shifts only letters by given amt
    ret = ''
    for x in message:
        changed = ord(x)
        if (65<=changed<=90): #changes capitals
            changed += shift
            if (changed<65):
                changed +=26
            if (changed>90):
                changed -=26
            ret = ret + chr(changed)
        elif(97<=changed<=122): #changes lowercase
            changed += shift
            if (changed<97):
                changed += 26
            if (changed>122):
                changed -= 26
            ret = ret + chr(changed)
        else:
            ret = ret + x #if not a letter
    return ret

def largestNumber(s): #finds largest num in string
    largest = 0
    num = 0 #amt of numbers
    for curr in s.split(): #splits into parts
        if (curr.isdigit()): #if curr is a number
            compare = int(curr)
            num+=1
            if(compare>largest): #if curr > current largest
                largest = compare
    if(num==0): #returns none if 0 numbers
        return None
    return largest

def topScorer(data):
    if(data==''): #tests for empty
        return None
    lists=data.splitlines()
    scoresAndNames=''
    currLargest=0
    for curr in lists: #goes through each person
        sum=0
        name=''
        for score in curr.split(','): #adds total score
            if(score.isdigit()):
                sum+=int(score)
            else: #records name
                name=score
            if (sum>currLargest): #finds largest score
                currLargest=sum
        scoresAndNames=scoresAndNames+str(sum)+','+name+"," #string of totals
    ret=''
    count=0
    for cur in scoresAndNames.split(','): #goes through final names/scores
        if(count==1): #if cur is a name
            ret=ret+cur+','
            count -=1
        if (cur.isdigit() and int(cur)==currLargest): #if highest score
            count+=1
    return ret[0:len(ret)-1]

#################################################
# Part B
#################################################

def collapseWhitespace(s): #replaces all cont whitespace w 1 space
    ret=''
    beforeIsSpace=False
    for x in s:
        if(beforeIsSpace==True): #checks if x b4 is a whitespace
            if(x=='\n' or x=='\t' or x.isspace()):
                continue
        if(x=='\n' or x=='\t' or x.isspace()): #removes whitespace
            ret=ret+' '
            beforeIsSpace=True
        else: #keeps non-whitespace
            ret=ret+x
            beforeIsSpace=False
    return ret

def patternedMessage(msg, pattern):
    msg = msg.replace(' ','')
    pattern = pattern.strip()
    curr = 0
    ret = ''
    for p in pattern:
        if(curr==len(msg)):
            curr=0
        if(p.isspace() or p=='\t' or p=='\n'):
            ret = ret+p
        else:
            ret = ret + msg[curr]
            curr+=1
    return ret

def charFinder(row, col, rows):
    return rows*col+row

def encodeRightLeftRouteCipher(text, rows):
    cols=math.ceil(len(text)/rows)
    currEnd=122 #ascii of last letter
    firstSol=''
    if(len(text)<cols*rows): #adds extra letters
        while(len(text)<cols*rows):
            text=text+chr(currEnd)
            currEnd-=1
        if (currEnd<97):
            currEnd=122
    for x in range(0, rows): #non-reversed row string
        firstSol=firstSol+'.'
        for y in range(0, cols):
            firstSol = firstSol + text[charFinder(x,y,rows)]
    finalSol=''
    curr=1
    for i in firstSol.split('.'): #reversed necessary rows
        if (curr%2==1):
            curr+=1
            finalSol=finalSol+i[::-1]
            continue
        curr+=1
        finalSol=finalSol+i
    return str(rows)+finalSol

def decodeRightLeftRouteCipher(cipher):
    rows=int(cipher[0])
    cipher=cipher[1:len(cipher)]
    cols=(len(cipher))//rows
    withPeriod='.'
    curr=0
    for x in cipher: #splits into groups by row
        if (curr==cols-1):
            curr=0
            withPeriod=withPeriod+x+'.'
        else:
            withPeriod=withPeriod+x
            curr+=1
    firstSol=''
    for i in withPeriod.split('.'): #reversed necessary rows
        if (curr%2==0):
            curr+=1
            firstSol=firstSol+i[::-1]
            continue
        curr+=1
        firstSol=firstSol+i
    finalSol=''
    for y in range(0, cols): #rearranges string
        for x in range(0, rows):
            finalSol=finalSol+firstSol[cols*x+y]
    finalfinalSol=''
    for p in finalSol: #removes non-capital letters
        if(ord(p)>=65 and ord(p)<=90):
            finalfinalSol=finalfinalSol+p
    return finalfinalSol

#################################################
# Part B Drawings
#################################################

# Make sure you have cmu_112_graphics downloaded to the 
# same directory as this file!

# Note: If you don't see any text when running graphics code, 
# try changing your computer's color theme to light mode. 

def drawFlagOfTheEU(canvas, x0, y0, x1, y1):
    canvas.create_rectangle(x0, y0, x1, y1, fill='yellow', outline='black')
    size = (x1 - x0) // 12
    canvas.create_text((x0 + x1)/2, (y0 + y1)/2, fill='black',
                       text='Draw the EU flag here!', font=f'Arial {size} bold')
    canvas.create_rectangle(x0,y0,x1,y1, fill='blue', outline='black')
    #my code below
    textSize=(x1-x0)//10
    canvas.create_text(x0+(x1-x0)/2,y0-(y1-y0)/10,text='European Union',
                        font=f'Arial{textSize}bold',fill='black')
    #draws blue flag and text above
    r=0.8*(y1-y0)/2
    midx=x0+(x1-x0)/4 #xposition to start circles
    midy=y0+(y1-y0)/16 #yposition to start circles
    for pos in range(12): #determines angle and rad to draw smaller circles
        ang=math.pi/2-(2*math.pi)*(pos/12)
        x=midx+r*math.cos(ang)
        y=midy-r*math.sin(ang)
        rc=(y1-y0)/2
        canvas.create_oval(x+r, y+r,x+rc, y+rc, fill='yellow')

def changeColor(color): #changes line color
    ret = color.replace('color','')
    count = 0
    for x in ret.split(' '):
        if (count>1):
            break
        else:
            ret = x
            count+=1
    ret = ret.strip()
    return ret

def removeExtra(string): #removes extra comments after command
    ret = ''
    count = 0
    for x in string.split(' '):
        if (count>1):
            break
        else:
            ret = x
            count+=1
    ret = ret.strip()
    return ret

def moveTortX(color, length, currDir): #moves x pos of tort
    if(color=='none'):
        xchange = math.cos(currDir)*int(length)
        return xchange
    else:
        xchange = math.cos(currDir)*int(length)
        return xchange

def moveTortY(color, length, currDir): #moves y pos of tort
    if(color=='none'):
        ychange = -1*math.sin(currDir)*int(length)
        return ychange
    else:
        ychange = -1*math.sin(currDir)*int(length)
        return ychange

#sorry it's rlly long the draw lines were like 3 lines each
def drawSimpleTortoiseProgram(program, canvas, width, height):
    currHeight=10
    textSize=10
    for line in program.split('\n'): #writes program
        canvas.create_text(10,currHeight,text=line,anchor='nw', 
                    font=f'Arial{textSize}bold',fill='gray')
        currHeight +=10
    currColor=''
    currX = width//2
    currY = height//2
    currDir = 0
    for currCom in program.split('\n'): #runs through program
        if (currCom.find('color')==-1 and currCom.find('move')==-1 and
            currCom.find('left')==-1 and currCom.find('right')==-1):
            continue
        #removes extra lines that aren't commands
        if 'color' in currCom: #changes color
            currColor = changeColor(currCom)
        elif 'move' in currCom: #moves line
            currCom = currCom.replace('move','')
            currCom = removeExtra(currCom)
            if(currColor=='none'): #changes pos w/o line
                currX += moveTortX(currColor, currCom.strip(),currDir)
                currY += moveTortY(currColor, currCom.strip(),currDir)
                continue
            canvas.create_line(currX, currY, currX+moveTortX(currColor, 
                currCom.strip(),currDir), currY+moveTortY(currColor,
                currCom.strip(),currDir),fill=f'{currColor}')
            currX += moveTortX(currColor, currCom.strip(),currDir)
            currY += moveTortY(currColor, currCom.strip(),currDir)
        elif 'left' in currCom: #rotates left
            currCom = currCom.replace('left','')
            currDir += float(int(currCom.strip()))*math.pi/180
        else: #rotates right
            currCom = currCom.replace('right','')
            currDir -= float(int(currCom.strip()))*math.pi/180

#################################################
# Bonus/Optional
#################################################

def bonusTopLevelFunctionNames(code):
    return 42

def bonusGetEvalSteps(expr):
    return 42

#################################################
# Test Functions
#################################################

def testRotateString():
    print("Testing rotateString()...", end="")
    assert(rotateString("abcde", 0) == "abcde")
    assert(rotateString("abcde", 1) == "bcdea")
    assert(rotateString("abcde", 2) == "cdeab")
    assert(rotateString("abcde", 3) == "deabc")
    assert(rotateString("abcde", 4) == "eabcd")
    assert(rotateString("abcde", 5) == "abcde")
    assert(rotateString("abcde", 25) == "abcde")
    assert(rotateString("abcde", 28) == "deabc")
    assert(rotateString("abcde", -1) == "eabcd")
    assert(rotateString("abcde", -2) == "deabc")
    assert(rotateString("abcde", -3) == "cdeab")
    assert(rotateString("abcde", -4) == "bcdea")
    assert(rotateString("abcde", -5) == "abcde")
    assert(rotateString("abcde", -25) == "abcde")
    assert(rotateString("abcde", -28) == "cdeab")
    print("Passed!")

def testApplyCaesarCipher():
    print("Testing applyCaesarCipher()...", end="")
    assert(applyCaesarCipher("abcdefghijklmnopqrstuvwxyz", 3) ==
                             "defghijklmnopqrstuvwxyzabc")
    assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
    assert(applyCaesarCipher("1234", 6) == "1234")
    assert(applyCaesarCipher("abcdefghijklmnopqrstuvwxyz", 25) ==
                             "zabcdefghijklmnopqrstuvwxy")
    assert(applyCaesarCipher("We Attack At Dawn", 2)  == "Yg Cvvcem Cv Fcyp")
    assert(applyCaesarCipher("We Attack At Dawn", 4)  == "Ai Exxego Ex Hear")
    assert(applyCaesarCipher("We Attack At Dawn", -1) == "Vd Zsszbj Zs Czvm")
    # And now, the whole point...
    assert(applyCaesarCipher(applyCaesarCipher('This is Great', 25), -25)
           == 'This is Great')
    print("Passed!")

def testLargestNumber():
    print("Testing largestNumber()...", end="")
    assert(largestNumber("I saw 3") == 3)
    assert(largestNumber("3 I saw!") == 3)
    assert(largestNumber("I saw 3 dogs, 17 cats, and 14 cows!") == 17)
    assert(largestNumber("I saw 3 dogs, 1700 cats, and 14 cows!") == 1700)
    assert(largestNumber("One person ate two hot dogs!") == None)
    print("Passed!")

def testTopScorer():
    print('Testing topScorer()...', end='')
    data = '''\
Fred,10,20,30,40
Wilma,10,20,30
'''
    assert(topScorer(data) == 'Fred')

    data = '''\
Fred,10,20,30
Wilma,10,20,30,40
'''
    assert(topScorer(data) == 'Wilma')

    data = '''\
Fred,11,20,30
Wilma,10,20,30,1
'''
    assert(topScorer(data) == 'Fred,Wilma')
    assert(topScorer('') == None)
    print('Passed!')

def testCollapseWhitespace():
    print("Testing collapseWhitespace()...", end="")
    assert(collapseWhitespace("a\nb") == "a b")
    assert(collapseWhitespace("a\n   \t    b") == "a b")
    assert(collapseWhitespace("a\n   \t    b  \n\n  \t\t\t c   ") == "a b c ")
    assert(collapseWhitespace("abc") == "abc")
    assert(collapseWhitespace("   \n\n  \t\t\t  ") == " ")
    assert(collapseWhitespace(" A  \n\n  \t\t\t z  \t\t ") == " A z ")
    print("Passed!")

def testPatternedMessage():
    print("Testing patternedMessage()...", end="")
    assert(patternedMessage("abc def",   "***** ***** ****")   ==
           "abcde fabcd efab")
    assert(patternedMessage("abc def", "\n***** ***** ****\n") == 
           "abcde fabcd efab")

    parms = [
    ("Go Pirates!!!", """
***************
******   ******
***************
"""),
    ("Three Diamonds!","""
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *
"""),
    ("Go Steelers!","""
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '$$$
   '$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
   o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$'
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
            '$$$o     '$$$$$$$$$$$$$$$$$$'$$'         $$$
              $$$o          '$$'$$$$$$'           o$$$
               $$$$o                                o$$$'
                '$$$$o      o$$$$$$o'$$$$o        o$$$$
                  '$$$$$oo     '$$$$o$$$$$o   o$$$$'
                     '$$$$$oooo  '$$$o$$$$$$$$$'
                        '$$$$$$$oo $$$$$$$$$$
                                '$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$'
                                      '$$$'
""")]
    solns = [
"""
GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira
"""
,
"""
    T     h     r
   eeD   iam   ond
  s!Thr eeDia monds
   !Th   ree   Dia
    m     o     n
"""
,
"""
                          GoSteelers!GoSteeler
                      s!GoSteelers!GoSteelers!GoS
                   teelers!GoSteelers!GoSteelers!GoS         te   el er
   s ! Go        Steelers!GoSteelers!GoSteelers!GoSteel       er s! GoSt
ee l e rs      !GoSteeler    s!GoSteelers!    GoSteelers       !GoSteel
ers!GoSte     elers!GoSt      eelers!GoSt      eelers!GoSt    eelers!G
  oSteele    rs!GoSteele      rs!GoSteele      rs!GoSteelers!GoSteeler
  s!GoSteelers!GoSteelers    !GoSteelers!G    oSteelers!GoSt  eele
   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSteel     ers!
    GoS   teelers!GoSteelers!GoSteelers!GoSteelers!GoSteelers     !GoSt
   eele   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSt       eele
   rs!    GoSteelers!GoSteelers!GoSteelers!GoSteelers!Go Steelers!GoSteele
  rs!GoSteelers  !GoSteelers!GoSteelers!GoSteelers!GoS   teelers!GoSteelers
  !GoSteelers!G   oSteelers!GoSteelers!GoSteelers!Go     Steel
 ers!       GoSt    eelers!GoSteelers!GoSteelers!G      oSte
            elers     !GoSteelers!GoSteelers!         GoS
              teel          ers!GoSteel           ers!
               GoSte                                elers
                !GoSte      elers!GoSteele        rs!Go
                  Steelers     !GoSteelers!   GoStee
                     lers!GoSte  elers!GoSteeler
                        s!GoSteele rs!GoSteel
                                ers!GoSteele
                                    rs!GoSteeler
                                     s!GoSteeler
                                      s!GoS
"""
    ]
    parms = [("A-C D?", """
*** *** ***
** ** ** **
"""),
    ("A", "x y z"),
    ("The pattern is empty!", "")
    ]
    solns = [
"""
A-C D?A -CD
?A -C D? A-
""",
"A A A",
""
    ]
    for i in range(len(parms)):
        (msg,pattern) = parms[i]
        soln = solns[i]
        soln = soln.strip("\n")
        observed = patternedMessage(msg, pattern)
        assert(observed == soln)
    print("Passed!")

def testEncodeRightLeftRouteCipher():
    print('Testing encodeRightLeftRouteCipher()...', end='')
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",4) ==
                                      "4WTAWNTAEACDzyAKT")
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",3) ==
                                      "3WTCTWNDKTEAAAAz") 
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",5) ==
                                      "5WADACEAKWNATTTz") 
    print('Passed!')

def testDecodeRightLeftRouteCipher():
    print('Testing decodeRightLeftRouteCipher()...', end='')
    assert(decodeRightLeftRouteCipher("4WTAWNTAEACDzyAKT") ==
                                      "WEATTACKATDAWN")
    assert(decodeRightLeftRouteCipher("3WTCTWNDKTEAAAAz") ==
                                      "WEATTACKATDAWN") 
    assert(decodeRightLeftRouteCipher("5WADACEAKWNATTTz") ==
                                      "WEATTACKATDAWN") 
    text = "WEATTACKATDAWN"
    cipher = encodeRightLeftRouteCipher(text, 6)
    plaintext = decodeRightLeftRouteCipher(cipher)
    assert(plaintext == text)
    print('Passed!')

def testBonusTopLevelFunctionNames():
    print("Testing bonusTopLevelFunctionNames()...", end="")

    # no fn defined
    code = """\
# This has no functions!
# def f(): pass
print("Hello world!")
"""
    assert(bonusTopLevelFunctionNames(code) == "")

    # f is redefined
    code = """\
def f(x): return x+42
def g(x): return x+f(x)
def f(x): return x-42
"""
    assert(bonusTopLevelFunctionNames(code) == "f.g")

    # def not at start of line
    code = """\
def f(): return "def g(): pass"
"""
    assert(bonusTopLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (''')
    code = """\
def f(): return '''
def g(): pass'''
"""
    assert(bonusTopLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (""")
    code = '''\
def f(): return """
def g(): pass"""
'''
    assert(bonusTopLevelFunctionNames(code) == "f")

    # triple-quote (''') in comment
    code = """\
def f(): return 42 # '''
def g(): pass # '''
"""
    assert(bonusTopLevelFunctionNames(code) == "f.g")

    # triple-quote (""") in comment
    code = '''\
def f(): return 42 # """
def g(): pass # """
'''
    assert(bonusTopLevelFunctionNames(code) == "f.g")

    # comment character (#) in quotes
    code = """\
def f(): return '#' + '''
def g(): pass # '''
def h(): return "#" + '''
def i(): pass # '''
def j(): return '''#''' + '''
def k(): pass # '''
"""
    assert(bonusTopLevelFunctionNames(code) == "f.h.j")
    print("Passed!")

def testBonusGetEvalSteps():
    print("Testing bonusGetEvalSteps()...", end="")
    assert(bonusGetEvalSteps("0") == "0 = 0")
    assert(bonusGetEvalSteps("2") == "2 = 2")
    assert(bonusGetEvalSteps("3+2") == "3+2 = 5")
    assert(bonusGetEvalSteps("3-2") == "3-2 = 1")
    assert(bonusGetEvalSteps("3**2") == "3**2 = 9")
    assert(bonusGetEvalSteps("31%16") == "31%16 = 15")
    assert(bonusGetEvalSteps("31*16") == "31*16 = 496")
    assert(bonusGetEvalSteps("32//16") == "32//16 = 2")
    assert(bonusGetEvalSteps("2+3*4") == "2+3*4 = 2+12\n      = 14")
    assert(bonusGetEvalSteps("2*3+4") == "2*3+4 = 6+4\n      = 10")
    assert(bonusGetEvalSteps("2+3*4-8**3%3") == """\
2+3*4-8**3%3 = 2+3*4-512%3
             = 2+12-512%3
             = 2+12-2
             = 14-2
             = 12""")
    assert(bonusGetEvalSteps("2+3**4%2**4+15//3-8") == """\
2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
                    = 2+81%16+15//3-8
                    = 2+1+15//3-8
                    = 2+1+5-8
                    = 3+5-8
                    = 8-8
                    = 0""")
    print("Passed!")

#################################################
# Graphics Test Functions
#################################################

def testDrawFlagOfTheEU(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill='lightYellow')
    drawFlagOfTheEU(canvas, 50, 125, 350, 275)
    drawFlagOfTheEU(canvas, 425, 100, 575, 200)
    drawFlagOfTheEU(canvas, 450, 275, 550, 325)
    canvas.create_text(app.width/2, app.height-25, fill='black',
                       text="Testing drawFlagOfTheEU")
    canvas.create_text(app.width/2, app.height-10, fill='black',
                       text="This does not need to resize properly!")

def testDrawSimpleTortoiseProgram(app, canvas, programName, program):
    drawSimpleTortoiseProgram(program, canvas, app.width, app.height)
    canvas.create_text(app.width/2, app.height-10, fill='black',
          text=(f'testing drawSimpleTortoiseProgram with {programName} ' + 
                f'(canvas, {app.width}, {app.height})'))

def testDrawSimpleTortoiseProgram_with_program_A(app, canvas):
    programA = '''\
# This is a simple tortoise program
color blue
move 50

left 90

color red
move 100

color none # turns off drawing
move 50

right 45

color green # drawing is on again
move 50

right 45

color orange
move 50

right 90

color purple
move 100'''
    testDrawSimpleTortoiseProgram(app, canvas, 'program A', programA)

def testDrawSimpleTortoiseProgram_with_program_B(app, canvas):
    programB = '''\
# Y
color red
right 45
move 50
right 45
move 50
right 180
move 50
right 45
move 50
color none # space
right 45
move 25

# E
color green
right 90
move 85
left 90
move 50
right 180
move 50
right 90
move 42
right 90
move 50
right 180
move 50
right 90
move 43
right 90
move 50  # space
color none
move 25

# S
color blue
move 50
left 180
move 50
left 90
move 43
left 90
move 50
right 90
move 42
right 90
move 50'''
    testDrawSimpleTortoiseProgram(app, canvas, 'program B', programB)

def drawSplashScreen(app, canvas):
    text = f'''\
Press the number key for the 
exercise you would like to test!

1. drawFlagOfTheEU
2. drawSimpleTortoiseProgram (with program A)
3. drawSimpleTortoiseProgram (with program B)

Press any other key to return
to this screen.
'''
    textSize = min(app.width,app.height) // 40
    canvas.create_text(app.width/2, app.height/2, text=text, fill='black',
                       font=f'Arial {textSize} bold')


def appStarted(app):
    app.lastKeyPressed = None
    app.timerDelay = 10**10

def keyPressed(app, event):
    app.lastKeyPressed = event.key

def redrawAll(app, canvas):
    if app.lastKeyPressed == '1':
      testDrawFlagOfTheEU(app, canvas)
    elif app.lastKeyPressed == '2':
      testDrawSimpleTortoiseProgram_with_program_A(app, canvas)
    elif app.lastKeyPressed == '3':
      testDrawSimpleTortoiseProgram_with_program_B(app, canvas)
    else:
      drawSplashScreen(app, canvas)

def testGraphicsFunctions():
    runApp(width=600, height=600)

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # Part A:
    testRotateString()
    testApplyCaesarCipher()
    testLargestNumber()
    testTopScorer()

    # Part B:
    testCollapseWhitespace()
    testPatternedMessage()
    testEncodeRightLeftRouteCipher()
    testDecodeRightLeftRouteCipher()

    # Part B Graphics:
    testGraphicsFunctions()

    # Bonus:
    # testBonusTopLevelFunctionNames()
    # testBonusGetEvalSteps()

def main():
    cs112_s22_week3_linter.lint()
    testAll()
    testGraphicsFunctions()

if __name__ == '__main__':
    main()
