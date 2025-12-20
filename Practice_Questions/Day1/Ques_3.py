# Leetcode Question No. 287 -> Find the Duplicate Number

# Complexity Analysis:
# Time Complexity: O(N), where N is the number of elements in the array.

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

# Example usage:
s = Solution()
nums = [1,3,4,2,2]
print(s.findDuplicate(nums)) # Output: 2