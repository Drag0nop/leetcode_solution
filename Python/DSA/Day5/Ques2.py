# N Queens: The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
# such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. 
# You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' 
# both indicate a queen and an empty space, respectively.

def solveNQueens(n):
    res = []
    board = [['.'] * n for _ in range(n)]
    cln = set()
    diag1 = set()
    diag2 = set()

    def backtrack(row):
        if row == n:
            res.append([''.join(r) for r in board])
            return
        for col in range(n):
            if col in cln or (row - col) in diag1 or (row + col) in diag2:
                continue
            board[row][col] = 'Q'
            cln.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            backtrack(row + 1)
            board[row][col] = '.'
            cln.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return res

# Example usage:
n = 4
print(solveNQueens(n))