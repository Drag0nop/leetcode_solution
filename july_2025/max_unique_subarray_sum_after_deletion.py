"""
You are given an integer array nums.

You are allowed to delete any number of elements from nums without making it empty. After performing the deletions, select a subarray of nums such that:

All elements in the subarray are unique.
The sum of the elements in the subarray is maximized.
Return the maximum sum of such a subarray.

Example :

Input: nums = [1,2,3,4,5]
Output: 15

Explanation:
Select the entire array without deleting any element to obtain the maximum sum.
"""

from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        n = len(nums)
        all = set(nums)
        mx = max(all)
        all.remove(mx)
        res = mx
        for i in all:
            res = max(res, res + i)
        return res

s = Solution()
print(s.maxSum([1, 2, 3, 4, 5]))