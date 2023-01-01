from array import array
import random
import numpy as np

def valid_cell(s, n: int, x: int, y: int):

    #check row
    for xx in range(0,9):
        if xx!=x and s[xx][y] == n:
            return False

    #check column
    for yy in range(0,9):
        if yy!=y and s[x][yy] == n:
            return False
    
    #check square
    for xs in range(x//3*3, x//3*3+3):
        for ys in range(y//3*3, y//3*3+3):
            if (not (xs==x and ys==y)) and s[xs][ys] == n:
                return False

    return True

def make_board(sboard):
    s = sboard
    for x in range(9):
        for y in range(9):
            if s[x][y] == 0:
                filled = False
                for n in range(1,10):
                    if valid_cell(s, n, x, y):
                        filled = True
                        s[x][y] = n
                        if make_board(s):
                            return True
                        else:
                            filled = False
                            s[x][y] = 0
                if not filled:
                    return False
    return True

# an array of all the available numbers
# a = [i for i in range(1,10)]
s = np.zeros((9,9))
make_board(s)
print(s)