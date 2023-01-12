#################################################
# hw9.py
#
# Your name: alanis zhao
# Your andrew id: aazhao
#################################################

import cs112_s22_week9_linter
import math, copy, os

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
# Functions for you to write
#################################################

def oddCount(L): #returns number of odds in L
    count=0
    if len(L)==0: #returns 0 if all elems checked
        return 0
    curr=L[0]
    if(curr%2==1): #if current is odd, add 1 to count
        count+=1
    L.pop(0)
    return oddCount(L)+count #count of rest of list + if curr elem is odd

def oddSum(L): #returns sum of all odd numbers in L
    added=0
    if len(L)==0: #returns 0 if all elems checked
        return 0
    curr=L[0]
    if(curr%2==1): #if current elem is odd, add to total sum
        added+=curr
    L.pop(0)
    return oddSum(L)+added #return sum of rest of list + curr elem if it's odd

def oddsOnly(L): #returns list of all odd numbers in list
    odds=[]
    if len(L)==0: #return empty list if all elems checked
        return []
    curr=L[0]
    if(curr%2==1): #if curr elem is odd, add to list
        odds+=[curr]
    L.pop(0)
    return odds+ oddsOnly(L) #return list of other odd elems + curr elem if odd

def maxOdd(L): #returns biggest odd number in list
    L=oddsOnly(L) #check only odd numbers
    if len(L)==0: #return None if all elems checked
        return None
    curr=L[0]
    L.pop(0)
    if (len(L)!=0): #as long as there are more elements left
        return max(curr, maxOdd(L)) #find greatest of curr elem or rest of list
    else:
        return curr #return last odd # for comparison
    
def hasConsecutiveDigits(n): #returns true if number has consec same digits
    if (n==0): #base case (if num is single dig or at end of recursion)
        return False
    else:
        curr=n%10
        n//=10
        if(curr==n%10): #check if current last digit = next digit
            return True
        else: #if not, keep checking number with current last digit removed
            return hasConsecutiveDigits(n)

def alternatingSum(L): #returns alternating sum of a list
    copyL=copy.copy(L)
    return returnAlternatingSum(copyL)

def returnAlternatingSum(L):
    if len(L)==0: #base case returns 0 if list is empty or checked
        return 0
    else:
        currDig=L[0] #check current digit
        L.pop(0)
        return currDig-alternatingSum(L)
        #causes minus sign to be flipped so every other elem adds

#################################################
# Freddy Fractal Viewer
#################################################
from cmu_112_graphics import *

#controller fxns
def appStarted(app):
    app.level=1 #curr level of fractal
    app.cx=app.width/2
    app.cy=app.height/2

def keyPressed(app, event):
    if event.key in ['Up','Right']: #increases app level
        app.level+=1
    elif (event.key in ['Down','Left']) and (app.level>0): 
        #decreases app level
        app.level-=1

#helper fxns
def returnRadius(app,level): #returns radius of curr level freddys
    return 0.5**level*app.width/4

def returnDistance(app,level): #dist of curr freddy level from center of view
    if(level==0):
        return 0
    else:
        return returnRadius(app,level)+returnDistance(app,level-1)

def rgbString(r, g, b): #from 112 website, turns hex into rgb
    return f'#{r:02x}{g:02x}{b:02x}'

#view fxns
def drawFractal(app, canvas, level, cx,cy, rad):
    if level == app.level+1: #draws up to current app level
        return
    else:
        drawFreddy(canvas,cx-rad,cy-rad,cx+rad,cy+rad) #draw current freddy
        drawFractal(app,canvas,level+1,cx-rad,cy-rad,rad/2)
        #draws left ear
        drawFractal(app,canvas,level+1,cx+rad,cy-rad,rad/2)
        #draws right ear

def drawFreddy(canvas,x1,y1,x2,y2): #draw freddy function in bounded box
    r=abs(x1-x2)/2 #radius of face
    centerX=(x1+x2)/2
    centerY=(y1+y2)/2
    canvas.create_oval(centerX-r,centerY-r,centerX+r,centerY+r,fill='brown',
                        width=r/10) #face in terms of center
    leftX,rightX=centerX-r/3,centerX+r/3
    eyeY=centerY-r/3
    lightbrown=rgbString(188, 158,130)
    canvas.create_oval(leftX-r/6,eyeY-r/6,leftX+r/6,eyeY+r/6,fill='black')
    #left and right eye
    canvas.create_oval(rightX-r/6,eyeY-r/6,rightX+r/6,eyeY+r/6,fill='black')
    canvas.create_oval(centerX-r/2.5,centerY,centerX+r/2.5,centerY+2*r/2.5,
                        fill = lightbrown, width=r/12) #snout
    canvas.create_oval(centerX-r/6,centerY-r/6+r/4,centerX+r/6,centerY+r/6+r/4,
                        fill='black') #nose
    canvas.create_arc(centerX-r/5,centerY+r/4+r/4,centerX,centerY+r/4+r/4+r/10,
                        style='arc',extent=-180,width=r/20) #left mouth
    canvas.create_arc(centerX,centerY+r/2,centerX+r/5,centerY+r/2+r/10,
                        style='arc',extent=-180,width=r/20) #right mouth

def redrawAll(app, canvas):
    margin=min(app.width, app.height)//10
    rad=returnRadius(app,0)
    drawFractal(app, canvas, 0, app.width/2,app.height/2+margin,rad)
    #draw base face --> recursively draws up to curr level
    canvas.create_text(app.width/2, 0,
                       text = f'Level {app.level} Fractal',
                       font = 'Arial ' + str(int(margin/3)) + ' bold',
                       anchor='n')
    canvas.create_text(app.width/2, margin,
                       text = 'Use arrows to change level',
                       font = 'Arial ' + str(int(margin/4)),
                       anchor='s')

def runFreddyFractalViewer():
    print('Running Freddy Fractal Viewer!')
    runApp(width=400, height=400)

#################################################
# Test Functions
#################################################

def testOddCount():
    print('Testing oddCount()...', end='')
    assert(oddCount([ ]) == 0)
    assert(oddCount([ 2, 4, 6 ]) == 0) 
    assert(oddCount([ 2, 4, 6, 7 ]) == 1)
    assert(oddCount([ -1, -2, -3 ]) == 2)
    assert(oddCount([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == 6)
    print('Passed!')

def testOddSum():
    print('Testing oddSum()...', end='')
    assert(oddSum([ ]) == 0)
    assert(oddSum([ 2, 4, 6 ]) == 0) 
    assert(oddSum([ 2, 4, 6, 7 ]) == 7)
    assert(oddSum([ -1, -2, -3 ]) == -4)
    assert(oddSum([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == 1+3+5+7+9+11)
    print('Passed!')

def testOddsOnly():
    print('Testing oddsOnly()...', end='')
    assert(oddsOnly([ ]) == [ ])
    assert(oddsOnly([ 2, 4, 6 ]) == [ ]) 
    assert(oddsOnly([ 2, 4, 6, 7 ]) == [ 7 ])
    assert(oddsOnly([ -1, -2, -3 ]) == [-1, -3])
    assert(oddsOnly([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == [1,3,5,7,9,11])
    print('Passed!')

def testMaxOdd():
    print('Testing maxOdd()...', end='')
    assert(maxOdd([ ]) == None)
    assert(maxOdd([ 2, 4, 6 ]) == None) 
    assert(maxOdd([ 2, 4, 6, 7 ]) == 7)
    assert(maxOdd([ -1, -2, -3 ]) == -1)
    assert(maxOdd([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == 11)
    print('Passed!')

def testHasConsecutiveDigits():
  print('Testing hasConsecutiveDigits()...', end='')
  assert(hasConsecutiveDigits(1123) == True)
  assert(hasConsecutiveDigits(-1123) == True)
  assert(hasConsecutiveDigits(1234) == False)
  assert(hasConsecutiveDigits(0) == False)
  assert(hasConsecutiveDigits(1233) == True)
  print("Passed!")

def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(alternatingSum([1,2,3,4,5]) == 1-2+3-4+5)
    assert(alternatingSum([ ]) == 0)
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    testOddCount()
    testOddSum()
    testOddsOnly()
    testMaxOdd()
    testHasConsecutiveDigits()
    testAlternatingSum()
    runFreddyFractalViewer()

def main():
    cs112_s22_week9_linter.lint()
    testAll()

if (__name__ == '__main__'):
    main()
