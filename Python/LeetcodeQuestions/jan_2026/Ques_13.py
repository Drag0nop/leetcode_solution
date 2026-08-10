# 3453. Separate Squares I

# Complexity Analysis:
# Time Complexity: O(N), where N is the number of squares.

from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # total area
        total_area = 0
        min_y = float('inf')
        max_y = float('-inf')

        for x, y, l in squares:
            total_area += l * l
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)

        half = total_area / 2.0

        def area_below(h):
            area = 0.0
            for x, y, l in squares:
                if h <= y:
                    continue
                elif h >= y + l:
                    area += l * l
                else:
                    area += l * (h - y)
            return area

        low, high = min_y, max_y
        eps = 1e-6

        while high - low > eps:
            mid = (low + high) / 2
            if area_below(mid) < half:
                low = mid
            else:
                high = mid

        return low
# Example usage:
s = Solution()
print(s.separateSquares([[0,0,2],[1,1,2]]))  # Output: 1.5(approx)