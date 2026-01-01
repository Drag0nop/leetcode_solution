# Leetcode Problem: 560. Subarray Sum Equals K

# Complexity Analysis:
# Time Complexity: O(N) where N is the length of the input array nums.


from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = defaultdict(int)
        res[0] = 1
        curr_sum = 0
        cnt = 0
        for i in nums:
            curr_sum += i

            if curr_sum - k in res:
                cnt += res[curr_sum - k]

            res[curr_sum] += 1

        return cnt