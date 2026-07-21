# 1390. Four Divisors
# Complexity Analysis
# Time Complexity: O(N∗Sqrt(M))
from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            temp = set()
            i = 1
            while i*i <= n:
                if n % i == 0:
                    temp.add(i)
                    temp.add(n // i)
                i += 1
            if len(temp) == 4:
                res += sum(temp)
        return res

# Example usage:
s = Solution()
print(s.sumFourDivisors([21, 4, 7]))  # Output: 32