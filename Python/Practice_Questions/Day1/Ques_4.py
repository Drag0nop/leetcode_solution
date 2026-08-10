# Leetcode Question No. 1 -> Two Sum

# Complexity Analysis:
# Time Complexity: O(N), where N is the number of elements in the array.
# Using Hash Map to store the difference values.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i,j in enumerate(nums):
            diff = target - j
            if diff in res:
                return [res[diff],i]
            res[j] = i

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9)) #output: [0, 1]