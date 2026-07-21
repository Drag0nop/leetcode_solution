# 2943. Maximize Area of Square Hole in Grid

# Complexity Analysis:
# Time Complexity: O(Nlogn+Mlogm), where N is the number of horizontal bars and M is the number of vertical bars. 
# Sorting the bar positions takes O(NlogN) and O(MlogM) time respectively. 
# The subsequent traversal to find the longest consecutive segments takes O(N) and O(M) time.

from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        def longest_consecutive(arr):
            if not arr:
                return 0
            arr.sort()
            longest = curr = 1
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    curr += 1
                    longest = max(longest, curr)
                else:
                    curr = 1
            return longest

        max_h = longest_consecutive(hBars) + 1
        max_v = longest_consecutive(vBars) + 1

        side = min(max_h, max_v)
        return side * side

# Example usage:
s = Solution()
print(s.maximizeSquareHoleArea(5, 5, [1, 2, 4], [0, 3]))  # Output: 4