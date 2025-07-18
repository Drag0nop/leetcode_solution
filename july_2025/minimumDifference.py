"""
You are given a 0-indexed integer array nums consisting of 3 * n elements.

You are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:

The first n elements belonging to the first part and their sum is sumfirst.
The next n elements belonging to the second part and their sum is sumsecond.
The difference in sums of the two parts is denoted as sumfirst - sumsecond.

For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.
Return the minimum difference possible between the sums of the two parts after the removal of n elements.

Example :

Input: nums = [3,1,2]
Output: -1
Explanation: Here, nums has 3 elements, so n = 1. 
Thus we have to remove 1 element from nums and divide the array into two equal parts.
- If we remove nums[0] = 3, the array will be [1,2]. The difference in sums of the two parts will be 1 - 2 = -1.
- If we remove nums[1] = 1, the array will be [3,2]. The difference in sums of the two parts will be 3 - 2 = 1.
- If we remove nums[2] = 2, the array will be [3,1]. The difference in sums of the two parts will be 3 - 1 = 2.
The minimum difference between sums of the two parts is min(-1,1,2) = -1.
"""
import heapq
import math
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        n1 = n // 3
        t1 = sum(nums[:n1])
        max_hp = [-x for x in nums[:n1]]
        heapq.heapify(max_hp)
        p1 = [0] * n
        p1[n1 - 1] = t1

        for i in range(n1, n1 * 2):
            t1 += nums[i]
            heapq.heappush(max_hp, -nums[i])
            t1 -= -heapq.heappop(max_hp)
            p1[i] = t1

        t2 = sum(nums[-n1:])
        min_hp = nums[-n1:]
        heapq.heapify(min_hp)
        p2 = [0] * n
        p2[n1 * 2] = t2

        for i in range(n1 * 2 - 1, n1 - 1, -1):
            t2 += nums[i]
            heapq.heappush(min_hp, nums[i])
            t2 -= heapq.heappop(min_hp)
            p2[i] = t2
        
        res = float('inf')
        for i in range(n1 - 1, n1 * 2):
            res = min(res, p1[i] - p2[i + 1])
        
        return res

s = Solution()
print(s.minimumDifference([3, 1, 2]))  # Output: -1