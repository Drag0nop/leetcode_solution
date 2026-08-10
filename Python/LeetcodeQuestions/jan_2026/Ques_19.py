# 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold

# Complexity Analysis:
# Time Complexity: O(M∗N∗Log(Min(M,N)))

from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # Build prefix sum
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    mat[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        def exists_square(k):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    total = (
                        prefix[i + k][j + k]
                        - prefix[i][j + k]
                        - prefix[i + k][j]
                        + prefix[i][j]
                    )
                    if total <= threshold:
                        return True
            return False

        low, high = 1, min(m, n)
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if exists_square(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
# Example usage:
s = Solution()
print(s.maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4)) # Output: 2