board = [[0 for _ in range(9)] for _ in range(9)]

def fill_board(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if fill_board(board):
                            return True
                        else:
                            board[row][col] = 0
                return False
    return True

def is_valid(board, row, col, num):
    # Check if the number is already in the row
    if num in board[row]:
        return False
    
    # Check if the number is already in the column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check if the number is already in the 3x3 sub-grid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

# You can then call the fill_board function to fill in the cells of the board
fill_board(board)

# You can print the board to the console to check that it has been filled in correctly
for row in board:
    print(row)
