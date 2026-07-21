# 3201. Find the Maximum Length of Valid Subsequence I

"""
You are given an integer array nums.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
Return the length of the longest valid subsequence of nums.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example :

Input: nums = [1,2,3,4]
Output: 4

Explanation:
The longest valid subsequence is [1, 2, 3, 4].
"""
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        dp = [[0, 0], [0, 0]]  # dp[last_parity][next_expected_parity]
        res = 0
        for i in nums:
            p = i & 1
            for j in (0, 1):
                dp[p][j] = dp[j][p] + 1
                res = max(res, dp[p][j])
        
        return res

s = Solution()
print(s.maximumLength([2, 39, 23]))  # output 2