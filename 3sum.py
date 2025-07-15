"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example :

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i,j in enumerate(nums):
            k = target - j
            if k in res:
                return [res[k], i]
            res[j] = i
        return []

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9)) #output: [0, 1]