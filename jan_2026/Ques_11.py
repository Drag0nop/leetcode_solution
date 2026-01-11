# 85. Maximal Rectangle

# Complexity Analysis:
# Time Complexity: O(M * N), where M and N are the number of rows and columns in the matrix.
# Space Complexity: O(N), where N is the number of columns in the matrix.

from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:
            # Build histogram
            for j in range(cols):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Largest rectangle in histogram
            stack = []
            for i in range(cols + 1):
                curr = heights[i] if i < cols else 0

                while stack and curr < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)

                stack.append(i)

        return max_area

# Example usage:
s = Solution()
print(s.maximalRectangle([
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]))  # Output: 6