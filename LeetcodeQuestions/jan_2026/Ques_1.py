# 66. Plus One

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits

# Example usage:
s = Solution()  
print(s.plusOne([1,2,3]))  # Output: [1,2,4]