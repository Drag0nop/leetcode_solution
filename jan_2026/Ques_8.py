# 1458. Max Dot Product of Two Subsequences

# Complexity Analysis
# Time Complexity: O(m * n), where m and n are the lengths of nums1

from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        NEG_INF = -10**18

        dp = [[NEG_INF] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                res = nums1[i-1] * nums2[j-1]

                dp[i][j] = max(
                    res + max(dp[i-1][j-1], 0),
                    dp[i-1][j],
                    dp[i][j-1]
                )
        return dp[n][m]

# Example usage:
s = Solution()
print(s.maxDotProduct([2,1,-2,5], [3,0,-6])) # Output: 18