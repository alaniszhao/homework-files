#alanis zhao
#aazhao

'''
style grading:
gabi's grade of mine:
-line 72: bad variable name: 'returned' (maybe try 'result')
-doesn't label functions as helper-fn's
-line 112 and 117: efficiency 'for i in range(0,value)' writing 0 is unnecessary

my grade of gabi's
-line 42 - don't use var name sum
-line 242-252 - could use description of what you are returning
-no other comments, she has good comments and variable names, consistent
spacing, uses helper fxns, efficient code :)
'''

import random

def gameDone(board): #checks if game is won
    for row in range(5):
        for col in range(5):
            if (board[row][col]==1): #game is still on if there are lights on
                return False
    return True

def printBoard(board): #prints board in format with row numbers
    rows = len(board)
    cols = len(board[0])
    print()
    # prints column headers
    print('    ', end='')
    print('  ', end='')
    for col in range(cols):
        print(str(col+1).center(3), ' ', end='')
    print()
    for row in range(rows): # prints board
        print('    ', end='')
        for col in range(cols):
            if col == 0:
                print(row+1,str(board[row][col]).center(3), ' ', end='')
            else:
                print(str(board[row][col]).center(3), ' ', end='')
        if row < rows-1:
            print('')    
        print()

def makeBoard(): #creates lights out board with random 0s and 1s
    returned = []
    for row in range(5):
        added=[]
        for col in range(5):
            added.append(random.randint(0,1))
        returned+=[added]
    return returned

def lightChange(row,col,board): #changes lights given position
    for r in range(5):
        for c in range(5):
            if (c==col and abs(row-r)<=1): #if adjacent row or on given position
                if(board[r][c]==1): #change to opposite
                    board[r][c]=0
                else:
                    board[r][c]=1
            elif (r==row and abs(col-c)<=1): #if adjacent column
                if(board[r][c]==1): #change to opposite
                    board[r][c]=0
                else:
                    board[r][c]=1

def lightsOut(): #runs lights out game
    print('0 is off, 1 is on')
    print('Rows and colums start at 1 and end at 5')
    board=makeBoard()
    done=False
    while(done==False): #while game is still unfinished
        printBoard(board)
        print('Which cell do you want to turn off?')
        resp=input('Input integer row and col number like row,col: ')
        rowResp=int(resp[0])-1
        colResp=int(resp[2])-1
        lightChange(rowResp,colResp,board) #changes lights based on player
        done=gameDone(board)
    if(done==True): #ends game
        printBoard(board)
        print('Good job you won!')

lightsOut()
