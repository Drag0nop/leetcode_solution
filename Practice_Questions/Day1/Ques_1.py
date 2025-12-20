# Leectcode Question No. 217 -> Contains Duplicate

# Complexity Analysis:
# Time Complexity: O(Nlogn), where n is the number of elements in the array.

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i = 0
        for j in range(1,len(nums)):
            if nums[i] == nums[j]:
                return True
            i += 1
        return False

# Example usage:
s = Solution()
nums = [1,2,3,1]
print(s.containsDuplicate(nums)) # Output: True