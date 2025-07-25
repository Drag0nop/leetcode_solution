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
        seen = set()
        max_sum = 0
        current_sum = 0
        start = 0
        
        for i in range(len(nums)):
            while nums[i] in seen:
                seen.remove(nums[start])
                current_sum -= nums[start]
                start += 1
            seen.add(nums[i])
            current_sum += nums[i]
            max_sum = max(max_sum, current_sum)
        
        return max_sum

s = Solution()
print(s.maxSum([1, 2, 3, 4, 5]))