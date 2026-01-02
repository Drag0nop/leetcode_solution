# 961. N-Repeated Element in Size 2N Array

from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(1,n):
            if nums[i - 1] == nums[i]:
                return nums[i]

# Example usage:
s = Solution()
print(s.repeatedNTimes([1,2,3,3]))  # Output: 3