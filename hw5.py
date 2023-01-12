#################################################
# hw5.py
# name: alanis zhao
# andrew id: aazhao
#################################################

import cs112_s22_week5_linter
import math, copy

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

def nondestructiveRemoveRowAndCol(A, row, col): #removes row and col nond
    rowResult = [0]*(len(A)) #creates list w 1 less row
    for rowI in range(len(A)): #loops through A
        if(rowI==row):
            continue
        else: #adds as long as it's not the selected row to remove
            rowResult[rowI]=A[rowI]
    rowResult.remove(0) #removes extra 0
    endResult=[]
    for row in rowResult: #loops through removed row list
        if(col==len(row)-1): #adds list w/o last elem if col is last col
            endResult.append(row[0:col])
        else: #appends split list based on col value
            endResult.append(row[0:col]+row[col+1:])
    return endResult

def destructiveRemoveRowAndCol(A, row, col): #removes row and col d
    A.pop(row) #removes row
    for currList in A: #goes through elems and removes col
        currList.pop(col)

def make2dList(rows, cols): #creates 2d list w 0s
    return [ ([0] * cols) for row in range(rows) ]

def matrixMultiply(m1,m2): #multiplies two matrices
    if(len(m1[0])!=len(m2)): #returns 0 if can't be multiplied
        return None
    ret=make2dList(len(m1),len(m2[0]))#list of 0 w m1 rows and m2 cols
    row1=0
    while (row1<=len(m1)-1): #loops through rows of m1
        col2=0
        while (col2<=len(m2[0])-1):#loops through cols of m2
            row2=0
            while (row2<=len(m2)-1): #loops through cols of m1 and rows of m2
                added=m1[row1][row2]*m2[row2][col2]
                ret[row1][col2]+=added
                row2+=1
            col2+=1
        row1+=1
    return ret

def retPos(board, num): #returns row and column of number on board
    for r in range(len(board)): #loops through rows
        for c in range(len(board[0])): #loops through columns
            if (board[r][c]==num):
                return r,c
    return -1,-1 #returns -1 if not in board

def inRange(lastR,lastP,currR,currP): #tests if in kings range
    if(abs(currR-lastR)==1 or abs(currP-lastP)==1):
        return True
    return False

def isKingsTour(board): #tests if a king could move in this order
    total=len(board)*len(board[0]) #number of moves
    lastrow,lastcol=retPos(board,1) #pos of first number
    for curr in range(2,total+1): #loops through number of moves
        currrow,currcol=retPos(board,curr)
        if(currrow==-1): #if skips a number return false
            return False
        if(inRange(lastrow,lastcol,currrow,currcol)==False):
            #if move isn't in range return false
            return False
        lastrow=currrow
        lastcol=currcol
    return True

#################################################
# Part B
#################################################

def noRepeats(a):#checks if 2d list has repeat elems
    currL=[]
    for row in range(len(a)):#goes through rows
        for col in range(len(a)):#goes through cols
            if (a[row][col] in currL):#matches w existing values
                return False
            else:
                currL+=[a[row][col]]
    return True

def horizSame(a,added):#checks if horiz sum of 2d=given value
    for row in range(len(a)):
        currsum=0
        for col in range(len(a)):
            currsum+=a[row][col]
        if(currsum!=added):
            return False
    return True

def verticSame(a,added):#checks if vertic sum of 2d=given value
    for col in range(len(a)):
        currsum=0
        for row in range(len(a)):
            currsum+=a[row][col]
        if(currsum!=added):
            return False
    return True

def diagSame(a,added):#checks both diag sums w given value
    rowCol=0
    add=0
    while(rowCol<len(a)):#checks top left to bottom right
        add+=a[rowCol][rowCol]
        rowCol+=1
    if(add!=added):
            return False
    add=0
    col=len(a)-1
    row=0
    while(col>=0):#checks top right to bottom left
        add+=a[row][col]
        col-=1
        row+=1
    if(add!=added):
            return False
    return True

def isMagicSquare(a):#return true if 2d list is magic square
    for row in range(len(a)):
        if(type(a[row])!=list): #checks if 2d list
            return False
        if(len(a)!=len(a[row])):#if not a square list
            return False
    for row in range(len(a)):#if not all int or if there are repeats
        for col in range(len(a)):
            if (type(a[row][col])!=int or noRepeats(a)==False):
                return False
    if(len(a)==1):#if there is only 1 value
        return True
    added=0
    for col in range(len(a)):#goes through and checks all sums
        added+=a[0][col]
    if(horizSame(a,added) and verticSame(a,added) and diagSame(a,added)):
        return True
    return False

def wordSearchWithIntegerWildcards(board, word): #from 112 website
    (rows, cols) = (len(board), len(board[0]))
    for row in range(rows):
        for col in range(cols):
            result = wordSearchFromCell(board, word, row, col)
            if (result != None):
                return True
    return False

def wordSearchFromCell(board, word, startRow, startCol): #from 112 website
    for drow in [-1, 0, +1]:
        for dcol in [-1, 0, +1]:
            if (drow, dcol) != (0, 0):
                result = wordSearchFromCellInDirection(board, word,
                                                       startRow, startCol,
                                                       drow, dcol)
                if (result != None):
                    return result
    return None

def wordSearchFromCellInDirection(board, word, startRow, startCol, drow, dcol):
    #if you can spell word in given dir
    (rows, cols) = (len(board), len(board[0]))
    dirNames = [ ["up-left"  ,   "up", "up-right"],
                 ["left"     ,   ""  , "right"   ],
                 ["down-left", "down", "down-right" ] ]
    index=0 #initial index
    index2=0 #determines row/col
    while (index <len(word)): #prevents index from being too long
        row = startRow + index2*drow
        col = startCol + index2*dcol
        if ((row < 0) or (row >= rows) or #if out of bounds
            (col < 0) or (col >= cols)):
            return None
        if (type(board[row][col])==str): #if no letters
            if ((board[row][col] != word[index])): #from 112 code
                return None
            index+=1
            if(abs(drow)>0 or abs(dcol)>0):
                index2+=1
        elif(type(board[row][col])==int): #if integer
            if(index+board[row][col]>len(word)): #from 112 code
                return None
            index+=board[row][col]
            if(abs(drow)>0 or abs(dcol)>0):
                index2+=1
    return (word, (startRow, startCol), dirNames[drow+1][dcol+1])

def areLegalValues(values):
    n2=len(values)
    n=0
    currVals=[]
    if(float(int(n2**0.5))==n2**0.5):
        n=int(n2**0.5)
    else: 
        return False
    for curr in values:
        if (curr>n2):
            return False
        if(currVals.count(curr)>0 and curr!=0):
            return False
        currVals+=[curr]
    return True

def isLegalRow(board, row):
    vals = []
    for c in range(len(board[row])):
        vals+=[board[row][c]]
    if areLegalValues(vals):
        return True
    return False

def isLegalCol(board, col):
    vals = []
    for r in range(len(board)):
        vals+=[board[r][col]]
    if areLegalValues(vals):
        return True
    return False

def isLegalBlock(board, block):
    n=int(len(board)**0.5)
    vals = []
    rowStart=0
    colStart=0
    if(block==0):
        rowStart=0
        colStart=0
    else:
        rowStart=block//n*n
        colStart=block%n*n
    for row in range(n):
        for col in range(n):
            vals+=[board[rowStart+row][colStart+col]]
    if areLegalValues(vals):
        return True
    return False

def isLegalSudoku(board):
    n2=len(board)
    for row in range(len(board)):
        if(isLegalRow(board,row)==False):
            return False
    for col in range(len(board[0])):
        if(isLegalCol(board,col)==False):
            return False
    for block in range(n2):
        if(isLegalBlock(board,block)==False):
            return False
    return True

#################################################
# Bonus/Optional
#################################################

def makeWordSearch(wordList, replaceEmpties):
    return 42

#################################################
# Test Functions (#ignore_rest)
#################################################

def testIsMagicSquare():
    print("Testing isMagicSquare()...", end="")
    assert(isMagicSquare([[42]]) == True)
    assert(isMagicSquare([[2, 7, 6], [9, 5, 1], [4, 3, 8]]) == True)
    assert(isMagicSquare([[4-7, 9-7, 2-7], [3-7, 5-7, 7-7], [8-7, 1-7, 6-7]])
           == True)
    a = [[7  ,12 ,1  ,14],
         [2  ,13 ,8  ,11],
         [16 ,3  ,10 ,5],
         [9  ,6  ,15 ,4]]
    assert(isMagicSquare(a))
    a=[42]
    assert(isMagicSquare(a)==False)
    a = [[113**2, 2**2, 94**2],
         [ 82**2,74**2, 97**2],
         [ 46**2,127**2,58**2]]
    assert(isMagicSquare(a) == False)
    a = [[  35**2, 3495**2, 2958**2],
         [3642**2, 2125**2, 1785**2],
         [2775**2, 2058**2, 3005**2]]
    assert(isMagicSquare(a) == False)
    assert(isMagicSquare([[1, 2], [2, 1]]) == False)
    assert(isMagicSquare([[0], [0]]) == False) # Not square!
    assert(isMagicSquare([[1, 1], [1, 1]]) == False) # repeats
    assert(isMagicSquare('do not crash here!') == False)
    assert(isMagicSquare(['do not crash here!']) == False)
    assert(isMagicSquare([['do not crash here!']]) == False)
    print("Passed!")

def testNondestructiveRemoveRowAndCol():
    print('Testing nondestructiveRemoveRowAndCol()...', end='')
    a = [ [ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]]
    aCopy = copy.copy(a)
    assert(nondestructiveRemoveRowAndCol(a, 1, 2) == [[2, 3, 5], [0, 1, 3]])
    assert(a == aCopy)
    assert(nondestructiveRemoveRowAndCol(a, 0, 0) == [[7, 6, 5], [1, 2, 3]])
    assert(a == aCopy)
    b = [[37, 78, 29, 70, 21, 62, 13, 54, 5],
    [6,     38, 79, 30, 71, 22, 63, 14, 46],
    [47,    7,  39, 80, 31, 72, 23, 55, 15],
    [16,    48, 8,  40, 81, 32, 64, 24, 56],
    [57,    17, 49, 9,  41, 73, 33, 65, 25],
    [26,    58, 18, 50, 1,  42, 74, 34, 66], 
    [67,    27, 59, 10, 51, 2,  43, 75, 35],
    [36,    68, 19, 60, 11, 52, 3,  44, 76],
    [77,    28, 69, 20, 61, 12, 53, 4,  45]]

    c = [[37, 78, 29, 70, 21, 62,     54, 5],
    [6,     38, 79, 30, 71, 22,     14, 46],
    [47,    7,  39, 80, 31, 72,     55, 15],
    [16,    48, 8,  40, 81, 32,     24, 56],
    [57,    17, 49, 9,  41, 73,     65, 25],
    [26,    58, 18, 50, 1,  42,     34, 66], 
    [67,    27, 59, 10, 51, 2,      75, 35],
    [36,    68, 19, 60, 11, 52, 44, 76]]

    bCopy = copy.copy(b)
    assert(nondestructiveRemoveRowAndCol(b,8,6) == c)
    assert(b == bCopy)
    print('Passed!')

def testDestructiveRemoveRowAndCol():
    print("Testing destructiveRemoveRowAndCol()...", end='')
    A = [ [ 2, 3, 4, 5],
          [ 8, 7, 6, 5],
          [ 0, 1, 2, 3]
        ]
    B = [ [ 2, 3, 5],
          [ 0, 1, 3]
        ]
    assert(destructiveRemoveRowAndCol(A, 1, 2) == None)
    assert(A == B) # but now A is changed!
    A = [ [ 1, 2 ], [3, 4] ]
    B = [ [ 4 ] ]
    assert(destructiveRemoveRowAndCol(A, 0, 0) == None)
    assert(A == B)
    A = [ [ 1, 2 ] ]
    B = [ ]
    assert(destructiveRemoveRowAndCol(A, 0, 0) == None)
    assert(A == B)
    print("Passed!")

def testMatrixMultiply():
    print("Testing matrixMultiply()...", end='')
    m1 = [[1,2],
          [3,4]] # 2x2
    m2 = [[4],
          [5]]     # 2x1
    m3 = [[14],
          [32]]
    assert(matrixMultiply(m1,m2) == m3) 
    assert(matrixMultiply([[3, 7], [4, 5], [5, 4], [5, 6], [8, 9], [7, 4]], 
                          [[9, 8, 3],
                           [5, 1, 3]])==
                          [[62, 31, 30],
                           [61, 37, 27],
                           [65, 44, 27],
                           [75, 46, 33],
                           [117, 73, 51],
                           [83, 60, 33]])
    assert matrixMultiply([[8]],[[5]])==[[40]]
    print("Passed!")

def testIsKingsTour():
    print("Testing isKingsTour()...", end="")
    a = [ [  3, 2, 1 ],
          [  6, 4, 9 ],
          [  5, 7, 8 ] ]
    assert(isKingsTour(a) == True)
    a = [ [  2, 8, 9 ],
          [  3, 1, 7 ],
          [  4, 5, 6 ] ]
    assert(isKingsTour(a) == True)
    a = [ [  7, 5, 4 ],
          [  6, 8, 3 ],
          [  1, 2, 9 ] ]
    assert(isKingsTour(a) == True)
    a = [ [  7, 5, 4 ],
          [  6, 8, 3 ],
          [  1, 2, 1 ] ]
    assert(isKingsTour(a) == False)
    a = [ [  3, 2, 9 ],
          [  6, 4, 1 ],
          [  5, 7, 8 ] ]
    assert(isKingsTour(a) == False)
    a = [ [  3, 2, 1 ],
          [  6, 4, 0 ],
          [  5, 7, 8 ] ]
    assert(isKingsTour(a) == False)
    a = [ [  1, 2, 3 ],
          [  7, 4, 8 ],
          [  6, 5, 9 ] ]
    assert(isKingsTour(a) == False)
    a = [ [ 3, 2, 1 ],
          [ 6, 4, 0 ],
          [ 5, 7, 8 ] ]
    assert(isKingsTour(a) == False)
    print("Passed!")

def testWordSearchWithIntegerWildcards():
    print("Testing wordSearchWithIntegerWildcards()...", end='')
    board = [ [ 'd', 'o', 'g' ],
              [ 't', 'a', 'c' ],
              [ 'o', 'a', 't' ],
              [ 'u', 'r', 'k' ],
            ]
    assert(wordSearchWithIntegerWildcards(board, "dog") == True)
    assert(wordSearchWithIntegerWildcards(board, "cat") == True)
    assert(wordSearchWithIntegerWildcards(board, "tad") == True)
    assert(wordSearchWithIntegerWildcards(board, "cow") == False)
    board = [ [ 'd', 'o',  1  ],
              [  3 , 'a', 'c' ],
              [ 'o', 'q' ,'t' ],
            ]
    assert(wordSearchWithIntegerWildcards(board, "z") == True)
    assert(wordSearchWithIntegerWildcards(board, "zz") == False)
    assert(wordSearchWithIntegerWildcards(board, "zzz") == True)
    assert(wordSearchWithIntegerWildcards(board, "dzzzo") == True)
    assert(wordSearchWithIntegerWildcards(board, "dzzo") == True)
    assert(wordSearchWithIntegerWildcards(board, "zzzd") == True)
    assert(wordSearchWithIntegerWildcards(board, "zzzo") == True)
    board = [ [ 3 ] ]
    assert(wordSearchWithIntegerWildcards(board, "zz") == False)
    assert(wordSearchWithIntegerWildcards(board, "zzz") == True)
    assert(wordSearchWithIntegerWildcards(board, "zzzz") == False)
    board = [ [ 'a', 'b', 'c' ],
              [ 'd',  2 , 'e' ],
              [ 'f', 'g', 'h' ]]
    assert(wordSearchWithIntegerWildcards(board, "aqqh") == True)
    assert(wordSearchWithIntegerWildcards(board, "aqqhh") == False)
    assert(wordSearchWithIntegerWildcards(board, "zz") == True)
    assert(wordSearchWithIntegerWildcards(board, "zzc") == True)
    assert(wordSearchWithIntegerWildcards(board, "zaz") == False)
    print("Passed!")

def testIsLegalSudoku():
    # From Leon Zhang!
    print("Testing isLegalSudoku()...", end="")
    board = [[0]]
    assert isLegalSudoku(board) == True
    board = [[1]]
    assert isLegalSudoku(board) == True

    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    assert isLegalSudoku(board) == True
    board = [[0, 4, 0, 0],
             [0, 0, 3, 0],
             [1, 0, 0, 0],
             [0, 0, 0, 2]]
    assert isLegalSudoku(board) == True
    board = [[1, 2, 3, 4],
             [3, 4, 1, 2],
             [2, 1, 4, 3],
             [4, 3, 2, 1]]
    assert isLegalSudoku(board) == True
    board = [[1, 2, 3, 4],
             [3, 4, 4, 2],
             [2, 4, 4, 3],
             [4, 3, 2, 1]]    
    assert isLegalSudoku(board) == False

    board = [
    [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
    [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
    [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
    [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
    [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
    [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
    [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
    [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
    [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
    ]
    assert isLegalSudoku(board) == True
    
    board = [
    [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
    [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
    [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
    [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
    [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
    [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
    [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
    [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
    [ 0, 0, 0, 0, 8, 0, 9, 7, 9 ]
    ]
    assert isLegalSudoku(board) == False
    board = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    assert isLegalSudoku(board) == True
    board = [
    [ 2,11, 9, 5, 8,16,13, 4,12, 3,14, 7,10, 6,15, 1],
    [ 4,12,15,10, 3, 6, 9,11,13, 5, 8, 1,16, 7,14, 2],
    [ 1,14, 6, 7,15, 2, 5,12,11, 9,10,16, 3,13, 8, 4],
    [16,13, 8, 3,14, 1,10, 7, 4, 6, 2,15, 9,11, 5,12],
    [12, 2,16, 9,10,14,15,13, 8, 1, 5, 3, 6, 4,11, 7],
    [ 6, 7, 1,11, 5,12, 8,16, 9,15, 4, 2,14,10, 3,13],
    [14, 5, 4,13, 6,11, 1, 3,16,12, 7,10, 8, 9, 2,15],
    [ 3, 8,10,15, 4, 7, 2, 9, 6,14,13,11, 1,12,16, 5],
    [13, 9, 2,16, 7, 8,14,10, 3, 4,15, 6,12, 5, 1,11],
    [ 5, 4,14, 6, 2,13,12, 1,10,16,11, 8,15, 3, 7, 9],
    [ 7, 1,11,12,16, 4, 3,15, 5,13, 9,14, 2, 8,10, 6],
    [10,15, 3, 8, 9, 5,11, 6, 2, 7, 1,12, 4,14,13,16],
    [11,10,13,14, 1, 9, 7, 8,15, 2, 6, 4, 5,16,12, 3],
    [15, 3, 7, 4,12,10, 6, 5, 1, 8,16,13,11, 2, 9,14],
    [ 8, 6, 5, 1,13, 3,16, 2,14,11,12, 9, 7,15, 4,10],
    [ 9,16,12, 2,11,15, 4,14, 7,10, 3, 5,13, 1, 6, 8]]
    assert isLegalSudoku(board) == True
    # last number is supposed to be 8, not 10
    board = [
    [ 2,11, 9, 5, 8,16,13, 4,12, 3,14, 7,10, 6,15, 1],
    [ 4,12,15,10, 3, 6, 9,11,13, 5, 8, 1,16, 7,14, 2],
    [ 1,14, 6, 7,15, 2, 5,12,11, 9,10,16, 3,13, 8, 4],
    [16,13, 8, 3,14, 1,10, 7, 4, 6, 2,15, 9,11, 5,12],
    [12, 2,16, 9,10,14,15,13, 8, 1, 5, 3, 6, 4,11, 7],
    [ 6, 7, 1,11, 5,12, 8,16, 9,15, 4, 2,14,10, 3,13],
    [14, 5, 4,13, 6,11, 1, 3,16,12, 7,10, 8, 9, 2,15],
    [ 3, 8,10,15, 4, 7, 2, 9, 6,14,13,11, 1,12,16, 5],
    [13, 9, 2,16, 7, 8,14,10, 3, 4,15, 6,12, 5, 1,11],
    [ 5, 4,14, 6, 2,13,12, 1,10,16,11, 8,15, 3, 7, 9],
    [ 7, 1,11,12,16, 4, 3,15, 5,13, 9,14, 2, 8,10, 6],
    [10,15, 3, 8, 9, 5,11, 6, 2, 7, 1,12, 4,14,13,16],
    [11,10,13,14, 1, 9, 7, 8,15, 2, 6, 4, 5,16,12, 3],
    [15, 3, 7, 4,12,10, 6, 5, 1, 8,16,13,11, 2, 9,14],
    [ 8, 6, 5, 1,13, 3,16, 2,14,11,12, 9, 7,15, 4,10],
    [ 9,16,12, 2,11,15, 4,14, 7,10, 3, 5,13, 1, 6,10]]
    assert isLegalSudoku(board) == False
    print("Passed!")

def testMakeWordSearch():
    print("Testing makeWordSearch()...", end="")
    board = makeWordSearch([], False)
    assert(board == None)

    board = makeWordSearch(["ab"], False)
    assert(board == [['a', 'b'], ['-', '-'] ])
    board = makeWordSearch(["ab"], True)
    assert(board == [['a', 'b'], ['c', 'd'] ])
    board = makeWordSearch(["ab", "bc", "cd"], False)
    assert(board == [['a', 'b'], ['c', 'd'] ])
    board = makeWordSearch(["ab", "bc", "cd", "de"], False)
    assert(board == [['a', 'b', '-'], ['c', 'd', '-'], ['d', 'e', '-']])
    board = makeWordSearch(["ab", "bc", "cd", "de"], True)
    assert(board == [['a', 'b', 'a'], ['c', 'd', 'c'], ['d', 'e', 'a']])

    board = makeWordSearch(["abc"], False)
    assert(board == [['a', 'b', 'c'], ['-', '-', '-'], ['-', '-', '-']])
    board = makeWordSearch(["abc"], True)
    assert(board == [['a', 'b', 'c'], ['c', 'd', 'a'], ['a', 'b', 'c']])

    board = makeWordSearch(["abc", "adc", "bd", "bef", "gfc"], False)
    assert(board == [['a', 'b', 'c'], ['d', 'e', '-'], ['c', 'f', 'g']])
    board = makeWordSearch(["abc", "adc", "bd", "bef", "gfc"], True)
    assert(board == [['a', 'b', 'c'], ['d', 'e', 'a'], ['c', 'f', 'g']])

    board = makeWordSearch(["abcd", "abc", "dcb"], False)
    assert(board == [['a', 'b', 'c', 'd'],
                     ['-', '-', '-', '-'], 
                     ['-', '-', '-', '-'],
                     ['-', '-', '-', '-']])
    board = makeWordSearch(["abcd", "abc", "dcb", "xa", "bya"], False)
    assert(board == [['a', 'b', 'c', 'd'],
                     ['x', 'y', '-', '-'], 
                     ['-', 'a', '-', '-'],
                     ['-', '-', '-', '-']])
    board = makeWordSearch(["abcd", "abc", "dcb", "xa", "bya", "bax", "dca"],
                           False)
    assert(board == [['a', 'b', 'c', 'd'],
                     ['x', 'y', 'c', '-'], 
                     ['-', 'a', '-', '-'],
                     ['-', '-', 'b', '-']])
    board = makeWordSearch(["abcd", "abc", "dcb", "xa", "bya", "bax", "dca"],
                           True)
    assert(board == [['a', 'b', 'c', 'd'],
                     ['x', 'y', 'c', 'a'], 
                     ['b', 'a', 'd', 'e'],
                     ['c', 'e', 'b', 'a']])

    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # Part A:
    testNondestructiveRemoveRowAndCol()
    testDestructiveRemoveRowAndCol()
    testMatrixMultiply()
    testIsKingsTour()

    # Part B:
    testIsMagicSquare()
    testWordSearchWithIntegerWildcards()
    testIsLegalSudoku()

    # Bonus:
    # testMakeWordSearch()

def main():
    cs112_s22_week5_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
