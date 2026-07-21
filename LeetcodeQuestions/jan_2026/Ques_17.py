# 3047. Find the Largest Area of Square Inside Two Rectangles

# Complexity Analysis:
# Time Complexity: O(N^2), where N is the number of sides of the rectangles.

from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_area = 0

        for i in range(n):
            x1, y1 = bottomLeft[i]
            x2, y2 = topRight[i]

            for j in range(i + 1, n):
                x3, y3 = bottomLeft[j]
                x4, y4 = topRight[j]

                # intersection rectangle
                left = max(x1, x3)
                bottom = max(y1, y3)
                right = min(x2, x4)
                top = min(y2, y4)

                if left < right and bottom < top:
                    width = right - left
                    height = top - bottom
                    side = min(width, height)
                    max_area = max(max_area, side * side)

        return max_area
    
# Example usage:
s = Solution()
print(s.largestSquareArea([[1,1],[2,2]], [[3,3],[4,4]])) # Output: 1