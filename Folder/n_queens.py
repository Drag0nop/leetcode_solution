# Leetcode Problem: N-Queens(LC -> 51)

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        soln = []
        board = [["."] * n for _ in range(n)]
        cln =set()
        diag1 = set()
        diag2 = set()
        
        def func(r):
            if r == n:
                soln.append(["".join(row) for row in board])
                return
            
            for i in range(n):
                if i in cln or (r - i) in diag1 or (r + i) in diag2:
                    continue

                board[r][i] = "Q"
                cln.add(i)
                diag1.add(r - i)
                diag2.add(r + i)

                func(r + 1)

                board[r][i] = "."
                cln.remove(i)
                diag1.remove(r - i)
                diag2.remove(r + i)
            
        func(0)
        return soln

sol = Solution()
print(sol.solveNQueens(4))