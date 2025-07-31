# 3480. Maximize Subarrays After Removing One Conflicting Pair

"""
You are given an integer n which represents an array nums containing the numbers from 1 to n in order. Additionally, you are given a 2D array conflictingPairs, 
where conflictingPairs[i] = [a, b] indicates that a and b form a conflicting pair.

Remove exactly one element from conflictingPairs. Afterward, count the number of non-empty subarrays of nums which do not contain both a and b for any 
remaining conflicting pair [a, b].

Return the maximum number of subarrays possible after removing exactly one conflicting pair.

Example :

Input: n = 4, conflictingPairs = [[2,3],[1,4]]
Output: 9

Explanation:
Remove [2, 3] from conflictingPairs. Now, conflictingPairs = [[1, 4]].
There are 9 subarrays in nums where [1, 4] do not appear together. They are [1], [2], [3], [4], [1, 2], [2, 3], [3, 4], [1, 2, 3] and [2, 3, 4].
The maximum number of subarrays we can achieve after removing one element from conflictingPairs is 9.
"""

from typing import List
from collections import defaultdict

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        limits = defaultdict(list)
        for a,b in conflictingPairs:
            limits[max(a, b)].append(min(a, b))
        
        res = 0
        left = [0, 0]
        removal = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in limits[i]:
                if j > left[0]:
                    left[1] = left[0]
                    left[0] = j
                elif j > left[1]:
                    left[1] = j
            res += i - left[0]
            removal[left[0]] += left[0] - left[1]

        return res + max(removal)


s = Solution()
print(s.maxSubarrays(4, [[2, 3], [1, 4]]))  # output: 9