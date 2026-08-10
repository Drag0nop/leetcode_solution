# 1266. Minimum Time Visiting All Points

# Complexity Analysis:
# Time Complexity: O(N), where N is the number of points.

from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]
            res += max(abs(x2 - x1),abs(y2 - y1))
        return res

# Example usage:
s = Solution()
print(s.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))  # Output: 7