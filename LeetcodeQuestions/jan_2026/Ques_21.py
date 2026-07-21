# 3315. Construct the Minimum Bitwise Array II
# Complexity Analysis:
# Time Complexity: O(n) where n is the length of nums

from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            if i != 2:
                res.append(i - (( i + 1) & (-i - 1)) // 2)
            else:
                res.append(-1)
        return res

# Example usage:
s = Solution()
print(s.minBitwiseArray([0, 2, 3, 5])) # Output: [0, -1, 1, 4]