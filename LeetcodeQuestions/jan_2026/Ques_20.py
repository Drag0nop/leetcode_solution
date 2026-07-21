# 3314. Construct the Minimum Bitwise Array I

# Complexity Analysis:
# Time Complexity: O(n * m) where n is the length of nums and m is the maximum value in nums

from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            curr = -1
            for c in range(nums[i]):
                if c | (c + 1) == nums[i]:
                    curr = c
                    break
            res.append(curr)
        return res

# Example usage:
s = Solution()
print(s.minBitwiseArray([0, 2, 3, 5])) # Output: [-1, -1, 1, 4]