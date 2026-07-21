# 2975. Maximum Square Area by Removing Fences From a Field
# Complexity Analysis:
# Time Complexity: O(M∗M+N∗N), where M is the number of horizontal fences and N is the number of vertical fences.

from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7

        # Add borders
        h = [1] + hFences + [m]
        v = [1] + vFences + [n]

        h.sort()
        v.sort()

        # All possible horizontal gaps
        h_gaps = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                h_gaps.add(h[j] - h[i])

        # All possible vertical gaps
        v_gaps = set()
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                v_gaps.add(v[j] - v[i])

        # Find largest common gap
        res = 0
        for gap in h_gaps:
            if gap in v_gaps:
                res = max(res, gap)

        if res == 0:
            return -1
        return (res * res) % MOD

# Example usage:
s = Solution()
print(s.maximizeSquareArea(6,7, [2], [4])) # Output: -1