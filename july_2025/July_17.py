# 3202. Find the Maximum Length of Valid Subsequence II

"""
You are given an integer array nums and a positive integer k.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
Return the length of the longest valid subsequence of nums.

Example :

Input: nums = [1,2,3,4,5], k = 2

Output: 5

Explanation:
The longest valid subsequence is [1, 2, 3, 4, 5].
"""

# complexity -> O(N∗K^2
from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]  # dp[last_remainder][next_expected_remainder]
        res = 0
        for i in nums:
            r = i % k
            for j in range(k):
                dp[r][j] = dp[j][r] + 1
                res = max(res, dp[r][j])
        
        return res

s = Solution()
print(s.maximumLength([1,4,2,3,1,4], 3))  # output: 4