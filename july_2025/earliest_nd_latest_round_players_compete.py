"""
There is a tournament where n players are participating. The players are standing in a single row and are numbered from 1 to n based on their initial standing position 
(player 1 is the first player in the row, player 2 is the second player in the row, etc.).

The tournament consists of multiple rounds (starting from round number 1). In each round, the ith player from the front of the row competes against the ith player from 
the end of the row, and the winner advances to the next round. When the number of players is odd for the current round, the player in the middle automatically advances 
to the next round.

For example, if the row consists of players 1, 2, 4, 6, 7
Player 1 competes against player 7.
Player 2 competes against player 6.
Player 4 automatically advances to the next round.
After each round is over, the winners are lined back up in the row based on the original ordering assigned to them initially (ascending order).

The players numbered firstPlayer and secondPlayer are the best in the tournament. They can win against any other player before they compete against each other. 
If any two other players compete against each other, either of them might win, and thus you may choose the outcome of this round.

Given the integers n, firstPlayer, and secondPlayer, return an integer array containing two values, the earliest possible round number and the latest possible round 
number in which these two players will compete against each other, respectively.

Example :

Input: n = 11, firstPlayer = 2, secondPlayer = 4
Output: [3,4]
Explanation:
One possible scenario which leads to the earliest round number:
First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
Second round: 2, 3, 4, 5, 6, 11
Third round: 2, 3, 4
One possible scenario which leads to the latest round number:
First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
Second round: 1, 2, 3, 4, 5, 6
Third round: 1, 2, 4
Fourth round: 2, 4
"""

# complexity -> O(2^n)

from functools import cache
from itertools import product
from typing import List

class Solution:
    def earliestAndLatest(self, n: int, f: int, s: int) -> List[int]:
        self.res = set()

        @cache
        def dfs(players, round):
            n = len(players)
            pairs = []
            for i in range(n//2):
                a = players[i]
                b = players[n - 1 - i]
                if a == f and b == s:
                    self.res.add(round)
                    return
                if not a in (f, s) and not b in (f, s):
                    pairs.append((a, b))
            
            to_add = (f, s) if n % 2 == 0 else tuple(set([f,s,players[n//2]]))
            
            for w in product(*pairs):
                next = sorted(w + to_add)
                dfs(tuple(next), round + 1)
            
        dfs(tuple(x for x in range(1, n + 1)), 1)
        return [min(self.res), max(self.res)]

sol = Solution()
print(sol.earliestAndLatest(11, 2, 4))  # Output: [3, 4]