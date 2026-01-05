# 1975. Maximum Matrix Sum
# Complexity Analysis
# Time Complexity: O(M * N), where M is the number of rows and N is the number of columns in the matrix.

from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res = negCount = 0
        mini = float('inf')
        for j in matrix:
            for i in j:
                res += abs(i)
                if i < 0:
                    negCount += 1
                mini = min(mini, abs(i))
        if negCount % 2 == 0:
            return res
        return res - 2 * mini 

# Example usage:
s = Solution()
print(s.maxMatrixSum([[1,-1],[-1,1]]))  # Output: 4