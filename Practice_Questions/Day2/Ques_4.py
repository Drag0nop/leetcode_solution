# LeetCode Problem: 53. Maximum Subarray
# Complexity Analysis:
# Time Complexity: O(N), where N is the number of elements in the input array.

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = greater = nums[0]
        for i in nums[1:]:
            curr = max(i, curr + i)
            greater = max(greater,curr)
        return greater

# Example usage:
s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6