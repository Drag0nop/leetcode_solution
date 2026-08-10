# 2044. Count Number of Maximum Bitwise-OR Subsets

"""
Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. 
Two subsets are considered different if the indices of the elements chosen are different.

The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).

Example :
Input: nums = [3,1]
Output: 2

Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
- [3]
- [3,1]
"""

# Complexity -> O(2^n)
from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        cnt = 0
        n = len(nums)
        # Calculate the maximum bitwise OR
        for num in nums:
            max_or |= num
        
        # Count subsets that yield the maximum bitwise OR
        def backtracking(index: int, curr: int):
            nonlocal cnt
            if index == n:
                if curr == max_or:
                    cnt += 1
                return
            
            # Include the current number
            backtracking(index + 1, curr | nums[index])
            # Exclude the current number
            backtracking(index + 1, curr)
        
        backtracking(0, 0)
        return cnt

s = Solution()
print(s.countMaxOrSubsets([3, 1]))  # output: 2