#################################################
# hw6.py
#
# Your name: alanis zhao
# Your andrew id: aazhao
#
# Your partner's name: gabi pimenta fujikawa
# Your partner's andrew id: gpimenta
#################################################

import cs112_s22_week6_linter
import math, copy, random

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
# Functions for you to write
#################################################

def isPerfectSquare(n): #checks if a number is a perfect square
    a=n**0.5 #square root
    if (a%1==0.0):
        return True
    return False

def isSortOfSquarish(n): #checks if a number is sort of squarish
    if (n<=0): #checks if pos
        return False
    test=n
    digits=[]
    while (test>0): #loops through and checks digits aren't 0
            last=test%10
            digits.append(last) #adds curr digit to a list
            if (last==0):
                return False
            test//=10
    if (isPerfectSquare(n)): #checks if num is perfect square
        return False
    digits=sorted(digits) #sorts list of digits
    sort=0
    for i in range(len(digits)): #remakes num as sorted digit int
        sort+=digits[i]*10**(len(digits)-i-1)
    if (isPerfectSquare(sort)==False): #checks if sorted int is perfect square
        return False
    return True

def nthSortOfSquarish(n): #finds the nth sort of squarish num
    guess=0
    found=0
    while (found<=n):#loops through while found is less than nth
        guess+=1
        if (isSortOfSquarish(guess)==True):
            found+=1
    return guess

#################################################
# s21-midterm1-animation
#################################################

def s22MidtermAnimation_appStarted(app): #initializes empty canvas
    app.timePassed=0
    app.r=10
    app.circleCenters=[]
    app.lines=[]
 
def s22MidtermAnimation_reset(app): #resets circles, lines, and time
    app.circleCenters=[]
    app.lines=[]
    app.timePassed=0
 
def s22MidtermAnimation_keyPressed(app, event): #resets if r is pressed
    if (event.key=='r'):
        s22MidtermAnimation_reset(app)
 
def s22MidtermAnimation_drawLines(app,canvas): #draws line to closest circle
    if (len(app.lines) < 2):
        return
    for line in app.lines: #loops through lines to draw
        x1,y1=line[0]
        x2,y2=line[1]
        canvas.create_line(x1,y1,x2,y2, fill='black')
 
def s22MidtermAnimation_drawCircles(app,canvas): #draws circles
    for circleCenter in app.circleCenters: #loops through circles to draw
        (cx,cy) = circleCenter
        r = app.r
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill='green')
 
def s22MidtermAnimation_getLines(app): #finds which circles to draw lines to
    app.lines = []
    for circleCenter1 in app.circleCenters:
        shortestDistance = 10000
        closestCircles = None
        for circleCenter2 in app.circleCenters:
            if circleCenter1 == circleCenter2: continue
            currentDist = getDistance(circleCenter1,circleCenter2)
            if  currentDist <= shortestDistance:
                shortestDistance = currentDist
                closestCircles = (circleCenter1,circleCenter2)
        if closestCircles != None:
            app.lines += [closestCircles]
 
def getDistance(circle1,circle2): #distance between 2 centers
    x1,y1 = circle1[0], circle1[1]
    x2,y2 = circle2[0], circle2[1]
    d = ((x2-x1)**2 + (y2-y1)**2)**.5
    return d
 
def s22MidtermAnimation_mousePressed(app,event): #adds circle to point
    newCircleCenters = (event.x, event.y)
    app.circleCenters.append(newCircleCenters)
 
def s22MidtermAnimation_timerFired(app): #keeps track of time
    s22MidtermAnimation_getLines(app)
    app.timePassed += app.timerDelay
    if app.timePassed > 5000: #resets if more than 5 sec between r presses
        s22MidtermAnimation_reset(app)
 
def s22MidtermAnimation_redrawAll(app, canvas): #draws circles and lines
    s22MidtermAnimation_drawCircles(app,canvas)
    s22MidtermAnimation_drawLines(app,canvas)
 
def s22Midterm1Animation():
    runApp(width=400, height=400, fnPrefix='s22MidtermAnimation_')

#################################################
# Tetris
#################################################

#draw functions
def drawFallingPiece(app,canvas): #draws current falling piece
    for row in range(len(app.fallingPiece)): #loops thru rows
        for col in range(len(app.fallingPiece[0])): #loops through cols
            if(app.fallingPiece[row][col]): #draws square if true
                drawCell(app,canvas,app.fallingPieceRow+row,
                app.fallingPieceCol+col,app.fallingPieceColor)

def drawScore(app,canvas): #draws curr score
    width=app.cols*app.cellSize+2*app.margin
    canvas.create_text(width/2, app.margin/2,text='Score: '+str(app.score))

def drawBoard(app, canvas): #draws board
    if(app.isGameOver):
        drawGameOver(app,canvas)
    height=app.rows*app.cellSize+2*app.margin
    width=app.cols*app.cellSize+2*app.margin
    canvas.create_rectangle(0,0,width,height,fill='orange')
    for currRow in range(len(app.board)): #goes cell by cell
        for currCol in range(len(app.board[0])):
            drawCell(app,canvas,currRow,currCol,app.board[currRow][currCol])

def drawGameOver(app,canvas): #draws game over sign
    height=app.rows*app.cellSize+2*app.margin
    width=app.cols*app.cellSize+2*app.margin
    canvas.create_rectangle(0,height/2.5,width,height/1.7,fill='white')
    canvas.create_text(width/2,height/2,text='Game Over',
                       fill='pink', font='Helvetica 26 bold underline')

def drawCell(app,canvas,row,col,color): #draws cell given parameters
    x1=app.margin+col*app.cellSize
    y1=app.margin+row*app.cellSize
    x2=x1+app.cellSize
    y2=y1+app.cellSize
    canvas.create_rectangle(x1,y1,x2,y2,fill=color,width=3)

def redrawAll(app,canvas): #draws all draw fxns
    drawBoard(app,canvas)
    drawFallingPiece(app,canvas)
    drawScore(app,canvas)
    if(app.isGameOver):
        drawGameOver(app,canvas)

#controller functions
def gameDimensions(): #sets size of game
    rows=15
    cols=10
    cellSize=20
    margin=25
    return rows,cols,cellSize,margin

def newFallingPiece(app): #creates random new falling piece
    import random
    randomIndex=random.randint(0,len(app.tetrisPieces)-1)
    app.fallingPiece=app.tetrisPieces[randomIndex]
    app.fallingPieceColor=app.tetrisPieceColors[randomIndex]
    app.fallingPieceRow=0
    app.fallingPieceCol=app.cols//2-len(app.fallingPiece[0])//2

def placeFallingPiece(app): #draws falling piece in app
    for row in range(len(app.fallingPiece)):
        for col in range(len(app.fallingPiece[0])):
            if(app.fallingPiece[row][col]):
                c=app.fallingPieceColor
                app.board[app.fallingPieceRow+row][app.fallingPieceCol+col]=c
    removeFullRows(app) #removes any full rows

def moveFallingPiece(app,drow,dcol): #moves falling piece L R or down
    app.fallingPieceRow+=drow
    app.fallingPieceCol+=dcol
    if(fallingPieceIsLegal(app)==False): #undo if illegal move
        app.fallingPieceRow-=drow
        app.fallingPieceCol-=dcol
        return False
    return True #returns if it was a legal move

def rotateFallingPiece(app): #rotates the falling piece
    oldPiece=copy.deepcopy(app.fallingPiece)
    oldRow=app.fallingPieceRow
    oldCol=app.fallingPieceCol
    newRows=len(oldPiece[0])
    newCols=len(oldPiece)
    new2D=[]
    for row in range(newRows): #creates new empty piece
        newRow=[]
        for col in range(newCols):
            newRow.append(None)
        new2D.append(newRow)
        newRow=[]
    currCol=0
    for row in range(newCols): #switches values of old piece to new one
        currRow=copy.copy(oldPiece[row])
        currRow.reverse()
        for newRow in range(newRows):
            new2D[newRow][currCol]=currRow[newRow]
        currCol+=1
    app.fallingPiece=new2D
    if(fallingPieceIsLegal(app)==False): #undo if move was illegal
        app.fallingPiece=oldPiece
        return
    newRow=oldRow+newCols//2-newRows//2
    newCol=oldCol+newRows//2-newCols//2
    app.fallingPieceRow=newRow #changes start row and col of piece
    app.fallingPieceCol=newCol
    if(fallingPieceIsLegal(app)==False): #undo if move was illegal
        app.fallingPieceRow=oldRow
        app.fallingPieceCol=oldCol
        app.fallingPiece=oldPiece
    
def fallingPieceIsLegal(app): #checks if piece in legal location
    for row in range(len(app.fallingPiece)):
        for col in range(len(app.fallingPiece[0])):
            if(app.fallingPiece[row][col]!=False):
                if (app.fallingPieceRow+row<0 or app.fallingPieceRow+row>=
                    app.rows):
                    return False #if row is in bounds
                if (app.fallingPieceCol+col<0 or app.fallingPieceCol+col>=
                    app.cols):
                    return False #if col in bounds
                if(app.board[app.fallingPieceRow+row][app.fallingPieceCol+col]
                    !='blue'):
                    return False #if cell is taken
    return True    

def removeFullRows(app): #removes full rows
    fullRows=0
    newBoard=[]
    notBlues=0
    for row in range(len(app.board)): #checks all cell colors
        for col in range(len(app.board[0])):
            if(app.board[row][col]=='blue'):
                newBoard.append(app.board[row])
                break
            notBlues+=1
        if(notBlues==len(app.board[0])): #full row if all colors not blue
            fullRows+=1
        notBlues=0
    fullRow=[]
    for i in range(len(app.board[0])): #creates empty row
        fullRow+=['blue']
    for i in range(fullRows): #inserts correct num of empty rows
        newBoard.insert(0,fullRow)
    app.board=newBoard
    app.score+=fullRows**2 #adds to score

def appStarted(app): #initiates tetris
    app.timerDelay = 250
    app.score=0
    app.rows,app.cols,app.cellSize,app.margin = gameDimensions()
    app.board=[]
    app.isGameOver=False
    for row in range(app.rows): #creates empty board
        currRow = []
        for col in range(app.cols):
            currRow+=['blue']
        app.board.append(currRow)
        currRow=[]
    iPiece = [[  True,  True,  True,  True ]]
    jPiece = [[  True, False, False ],[  True,  True,  True ]]
    lPiece = [[ False, False,  True ],[  True,  True,  True ]]
    oPiece = [[  True,  True ],[  True,  True ]]
    sPiece = [[ False,  True,  True ],[  True,  True, False ]]
    tPiece = [[ False,  True, False ],[  True,  True,  True ]]
    zPiece = [[  True,  True, False ],[ False,  True,  True ]]
    app.tetrisPieces=[iPiece,jPiece,lPiece,oPiece,sPiece,tPiece,zPiece]
    app.tetrisPieceColors=["red","yellow","magenta","pink","cyan","green"
                            ,"orange"]
    newFallingPiece(app) #starts new falling piece

def keyPressed(app, event): #controls
    if event.key=='r': #restarts
            appStarted(app)
    if(app.isGameOver!=True):
        if event.key=='Up': #rotates piece
            rotateFallingPiece(app)
        if event.key=='Down': #moves down 1 cell
            moveFallingPiece(app,1,0)
        if event.key=='Left': #moves left 1 cell
            moveFallingPiece(app,0,-1)
        if event.key=='Right': #moves right one cell
            moveFallingPiece(app,0,1) 
        if event.key=='Space': #hard drops piece
            hardDrop(app)

def hardDrop(app): #moves piece as far down as possible
    while (moveFallingPiece(app,1,0)==True):
        moveFallingPiece(app,1,0)

def timerFired(app): #runs timed fuctions
    if(app.isGameOver==False):
        if(moveFallingPiece(app,+1,0)==False): #moves and places legal piece
            placeFallingPiece(app)
            newFallingPiece(app)
            if(moveFallingPiece(app,+1,0)==False): #ends game if no legal moves
                app.isGameOver=True

def playTetris(): #runs tetris
    rows,cols,cellSize,margin=gameDimensions()
    w = cols*cellSize+2*margin
    h = rows*cellSize+2*margin
    runApp(width=w, height=h)

#################################################
# Test Functions
#################################################

def testIsPerfectSquare():
    print('Testing isPerfectSquare(n))...', end='')
    assert(isPerfectSquare(4) == True)
    assert(isPerfectSquare(9) == True)
    assert(isPerfectSquare(10) == False)
    assert(isPerfectSquare(225) == True)
    assert(isPerfectSquare(1225) == True)
    assert(isPerfectSquare(1226) == False)
    print('Passed')


def testIsSortOfSquarish():
    print('Testing isSortOfSquarish(n))...', end='')
    assert(isSortOfSquarish(52) == True)
    assert(isSortOfSquarish(16) == False)
    assert(isSortOfSquarish(502) == False)
    assert(isSortOfSquarish(414) == True)
    assert(isSortOfSquarish(5221) == True)
    assert(isSortOfSquarish(6221) == False)
    assert(isSortOfSquarish(-52) == False)
    print('Passed')


def testNthSortOfSquarish():
    print('Testing nthSortOfSquarish()...', end='')
    assert(nthSortOfSquarish(0) == 52)
    assert(nthSortOfSquarish(1) == 61)
    assert(nthSortOfSquarish(2) == 63)
    assert(nthSortOfSquarish(3) == 94)
    assert(nthSortOfSquarish(4) == 252)
    assert(nthSortOfSquarish(8) == 522)
    print('Passed')

def testAll():
    testIsPerfectSquare()
    testIsSortOfSquarish()
    testNthSortOfSquarish()

#################################################
# main
#################################################

def main():
    cs112_s22_week6_linter.lint()
    testAll()
    s22Midterm1Animation()
    playTetris()

if __name__ == '__main__':
    main()
