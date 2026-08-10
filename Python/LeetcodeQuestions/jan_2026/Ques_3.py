# 1411. Number of Ways to Paint N × 3 Grid
# Complexity Analysis
# Time Complexity: O(N) where N is the number of rows in the grid.

class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        same = diff = 6
        for _ in range(2, n + 1):
            new = (same * 3 + diff * 2) % MOD
            new_diff = (same * 2 + diff * 2) % MOD
            same, diff = new, new_diff
        return (same + diff) % MOD

# Example usage:
s = Solution()
print(s.numOfWays(1))  # Output: 12