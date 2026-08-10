# Leetcode Question No. 169 -> Majority Element
# Complexity Analysis:
# Time Complexity: O(N), where N is the number of elements in the input array.

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        k = None
        for i in nums:
            if cnt == 0:
                k = i
            cnt += 1 if i == k else -1
        return k

# Example usage:
s = Solution()
print(s.majorityElement([3,2,3]))  # Output: 3