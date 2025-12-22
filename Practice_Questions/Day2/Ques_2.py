# Leetcode Question No. 724 -> Find Pivot Index

# Complexity Analysis:
# Time Complexity: O(N), where N is the number of elements in the input array. We traverse the array twice.

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for i,j in enumerate(nums):
            if left == total - left - j:
                return i
            left += j
        return -1

# Example usage:
s = Solution()
print(s.pivotIndex([1,7,3,6,5,6]))  # Output: 3