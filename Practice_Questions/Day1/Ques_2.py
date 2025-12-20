# Leetcode Question no.26 -> Remove Duplicates from Sorted Array

# Complexity Analysis:
# Time Complexity: O(n), where n is the number of elements in the array.

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k

# Example usage:
s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(nums)) # Output: 5