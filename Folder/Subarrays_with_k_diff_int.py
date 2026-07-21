"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.
A good array is an array where the number of different integers in that array is exactly k.
For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
"""

from typing import List
from collections import defaultdict

# option 1(Runtime 143 ms)
class Solution:
    def countAtMostK(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        count = 0
        distinct = 0

        for right in range(len(nums)):
            if freq[nums[right]] == 0:
                distinct += 1
            freq[nums[right]] += 1

            while distinct > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    distinct -= 1
                left += 1

            count += right - left + 1

        return count

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.countAtMostK(nums, k) - self.countAtMostK(nums, k - 1)

# ============================================================================


# option 2 (Best way to do: Runtime 1ms)
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(arr, k):
            l = 0
            count = 0
            freq = defaultdict(int)
            
            for r in range(len(arr)):
                freq[arr[r]] += 1
                while len(freq) > k:
                    freq[arr[l]] -= 1
                    if freq[arr[l]] == 0:
                        del freq[arr[l]]
                    l += 1
                count += r - l + 1
            return count

        return atMostK(nums, k) - atMostK(nums, k - 1)


sol = Solution()
print(sol.subarraysWithKDistinct([1, 2, 1, 2, 3], 2))  # Output: 7