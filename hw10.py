#################################################
# hw10.py
#
# Your name: alanis zhao
# Your andrew id: aazhao
#################################################

import cs112_s22_week10_linter
import math, os

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

def findLargestFile(path): #wrapper fxn
    results=findLargestFileAndSize(path) #tuple of best path and size
    return results[0] #returns path

def findLargestFileAndSize(path): #helper fxn for findLargestFile
    bestSize=0
    bestPath=''
    for curr in os.listdir(path): #loop through everything in curr folder
        check=path+'/'+curr
        if(os.path.isdir(check)==False): #if it's a file
            currSize=os.path.getsize(check) #get the size
            if(currSize>bestSize): #set best size and path if it's the biggest
                bestSize=currSize
                bestPath=check
        elif(os.path.isdir(check)==True): #if it's a folder
            results=findLargestFileAndSize(check) #recurs check that folder
            if(results[1]>bestSize): 
                #set best size and path if biggest in that folder
                bestSize=results[1]
                bestPath=results[0]
    return (bestPath,bestSize)

def knightsTour(rows, cols): #return valid knights tour for list w rows and cols
    for r in range(rows): #loop through starting rows 
        for c in range (cols): #loops through starting cols
            emptyBoard=[([0]*cols) for row in range(rows)]
            emptyBoard[r][c]=1
            possSol=knightsSol(r,c,emptyBoard,1) #check current startpoint
            if(possSol!=None): #return if possible solution
                return possSol
    return None

def validBoard(board): #check if a board is valid
    rowStart,colStart=None,None
    moves=len(board)*len(board[0]) #number of moves needed to complete
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c]==0: #if it's not complete return false
                return False
            if board[r][c]==1: #find starting point
                rowStart=r
                colStart=c
    possMoves=[(2,1),(2,-1),(-1,2),(-1,-2),(-2,-1),(-2,1),(1,2),(1,-2)]
    #possible knight moves
    for currNum in range(2,moves+1): #run through rest of moves
        for (dx,dy) in possMoves:
            currR=rowStart+dx
            currC=colStart+dy
            if(currR<len(board) and currR>=0 and currC<len(board[0]) and
                currC>=0): #if in bounds
                if(board[currR][currC]==currNum): #if it is next move
                    rowStart=currR
                    colStart=currC
                    break #start w next move
            else:
                if(dx==1 and dy==-2): #see if all moves checked
                    return False
    return True  

def knightsSol(row,col,board,move): #returns solution for current board
    if validBoard(board): #if the board is done, return it
        return board
    moves=[(2,1),(2,-1),(-1,2),(-1,-2),(-2,-1),(-2,1),(1,2),(1,-2)]
    #possible knight moves
    for (dx,dy) in moves:
        newRow=row+dx
        newCol=col+dy
        if(newRow<len(board) and newRow>=0 and newCol<len(board[0]) and
            newCol>=0 and board[newRow][newCol]==0):
            #if in bounds and empty space
                board[newRow][newCol]=move+1 #move the knight
                result=knightsSol(newRow,newCol,board,move+1)
                #check rest of board from this move
                if result!=None: #if it is solution then return it
                    return board
                board[newRow][newCol]=0 #resets move if not valid solution
    return None

#################################################
# Test Functions
#################################################

def testFindLargestFile():
    print('Testing findLargestFile()...', end='')
    assert(findLargestFile('sampleFiles/folderA') ==
                           'sampleFiles/folderA/folderC/giftwrap.txt')
    assert(findLargestFile('sampleFiles/folderB') ==
                           'sampleFiles/folderB/folderH/driving.txt')
    assert(findLargestFile('sampleFiles/folderB/folderF') == '')
    print('Passed!')

def testKnightsTour():
    print('Testing knightsTour()....', end='')
    def checkDims(rows, cols, ok=True):
        T = knightsTour(rows, cols)
        s = f'knightsTour({rows},{cols})'
        if (not ok):
            if (T is not None):
                raise Exception(f'{s} should return None')
            return True
        if (T is None):
            raise Exception(f'{s} must return a {rows}x{cols}' +
                             ' 2d list (not None)')
        if ((rows != len(T)) or (cols != (len(T[0])))):
            raise Exception(f'{s} must return a {rows}x{cols} 2d list')
        d = dict()
        for r in range(rows):
            for c in range(cols):
                d[ T[r][c] ] = (r,c)
        if (sorted(d.keys()) != list(range(1, rows*cols+1))):
            raise Exception(f'{s} should contain numbers' +
                             ' from 1 to {rows*cols}')
        prevRow, prevCol = d[1]
        for step in range(2, rows*cols+1):
            row,col = d[step]
            distance = abs(prevRow - row) + abs(prevCol - col)
            if (distance != 3):
                raise Exception(f'{s}: from {step-1} to {step}' +
                                 ' is not a legal move')
            prevRow, prevCol = row,col
        return True
    assert(checkDims(4, 3))
    assert(checkDims(4, 4, ok=False))
    assert(checkDims(4, 5))
    assert(checkDims(3, 4))
    assert(checkDims(3, 6, ok=False))
    assert(checkDims(3, 7))
    assert(checkDims(5, 5))
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    testFindLargestFile()
    testKnightsTour()

def main():
    cs112_s22_week10_linter.lint()
    testAll()

if (__name__ == '__main__'):
    main()