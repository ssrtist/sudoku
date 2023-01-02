from array import array
import random
import numpy as np

def valid_cell(s, n: int, x: int, y: int):

    # 0 is invalid
    if n == 0:
        return False

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

s = np.zeros((9,9))
x = 0
y = 0
while True:
    s[x][y]+=1
    while s[x][y]<=9:
        if valid_cell(s, s[x][y], x, y):
            if x==8 and y==8:
                print(f'x={x}, y={y}, s[{x}][{y}]={s[x][y]}')
                print('Puzzle filled')
                print(s)
                quit()

            # move to next cell
            x+=1
            if x>8:
                y+=1
                x=0
                if y>8:
                    print('Failed to generate puzzle (y > 8)')
                    quit()
            break
        else:
            s[x][y]+=1

    # if there's no valid number go back one cell
    if s[x][y]>9:
        s[x][y]=0
        x-=1
        if x<0: 
            y-=1
            x=8
            if y<0:
                print('All iterations complete')
                break
        # break
print(s)