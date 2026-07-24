# Sudoku Solver: Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
#  1. Each of the digits 1-9 must occur exactly once in each row.
#  2. Each of the digits 1-9 must occur exactly once in each column.
#  3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

# The '.' character indicates empty cells.

def solve_sudoku(board):
    rows = [set() for i in range(9)]
    cols = [set() for i in range(9)]
    boxes = [set() for i in range(9)]
    empty = []

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                empty.append([r,c])
            else:
                num = board[r][c]
                rows[r].add(num)
                cols[c].add(num)
                boxes[(r // 3) * 3 + (c // 3)].add(num)

    def backtrack(path):
        if path == len(empty):
            return True
        
        row,col = empty[path]
        boxIndex = (row // 3) * 3 + (col // 3)
        for char in "123456789":
            if (char not in rows[row] and char not in cols[col] and char not in boxes[boxIndex]):
                board[row][col] = char
                rows[row].add(char)
                cols[col].add(char)
                boxes[boxIndex].add(char)
                if backtrack(path+1):
                    return True
                board[row][col] = '.'
                rows[row].remove(char)
                cols[col].remove(char)
                boxes[boxIndex].remove(char)
        return False

    backtrack(0)

# Example usage:
sudoku_board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '6', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]
solve_sudoku(sudoku_board)
for row in sudoku_board:
    print(row)