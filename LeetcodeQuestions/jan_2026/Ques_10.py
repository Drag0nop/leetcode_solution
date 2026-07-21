# 712. Minimum ASCII Delete Sum for Two Strings

# Complexity Analysis:
# Time Complexity: O(M * N), where M and N are the lengths of the two

from typing import List

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        # Base case
        for i in range(1, n + 1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])

        for j in range(1, m + 1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        # Fill DP
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j] + ord(s1[i-1]),
                        dp[i][j-1] + ord(s2[j-1])
                    )

        return dp[n][m]

# Example usage:
s = Solution()
print(s.minimumDeleteSum("sea", "eat"))  # Output: 231