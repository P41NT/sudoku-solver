file= open('board.txt', 'r').read()
board = [list(map(int, list(row))) for row in file.split('\n')]

def empty_(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i , j)
    return None

def solve(board):
    empty = empty_(board)
    if not empty:
        return True
    else:
        row, col = empty
    for i in range(1, 10):
        if valid(board, i, row, col):
            board[row][col] = i
            ans = solve(board)
            if ans:
                return True
            board[row][col] = 0
    return False

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def valid(board, num, row, col):
    for i in range(len(board[0])):
        if board[row][i] == num and col != i:
            return False
    for i in range(len(board)):
        if board[i][col] == num and row != i:
            return False
    box_row = row//3
    box_col = col//3
    for i in range(box_row*3, box_row*3 + 3):
        for j in range(box_col * 3, box_col*3 + 3):
            if board[i][j] == num and (i,j) != (col, row):
                return False
    return True

print_board(board)
solve(board)
print('---------------------------')
print_board(board)
