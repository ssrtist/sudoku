from array import array
import random
import numpy as np

def valid_cell(s, n: int, x: int, y: int):

    #check row
    for xx in range(0,9):
        if xx!=x and s[xx][y] == n:
            #print(f"{n} conflicts with {xx}, {y} ({int(s[xx][y])})")
            return False

    #check column
    for yy in range(0,9):
        if yy!=y and s[x][yy] == n:
            #print(f"{n} conflicts with {x}, {yy} ({int(s[x][yy])})")
            return False
    
    #check square
    #for a in range(c//3*3,c//3*3+3):
    for xs in range(x//3*3, x//3*3+3):
        for ys in range(y//3*3, y//3*3+3):
            #print(f"checking cell({xs},{ys})")
            if (not (xs==x and ys==y)) and s[xs][ys] == n:
                return False

    return True

def make_board(sboard, x, y):
    if x>8 or y>8:
        return
    s = sboard
    found = False
    for n in range(1,10):
        print(f"testing {n} in {x}, {y}")
        if valid_cell(s, n, x, y):
            found = True
            s[x][y] = n
            print(f"{n} fits cell {x}, {y}")
            make_board(s, x+1, y)
            make_board(s, x, y+1)
        print('current board:')
        print(s)
    if not found:
        print(f'failed to generate board at {x}, {y}')
        print('current board:')
        print(s)
        return
    # return

# an array of all the available numbers
a = array('b', [i for i in range(1,10)])
s = np.zeros((9,9))
b = make_board(s, 0, 0)    
quit()