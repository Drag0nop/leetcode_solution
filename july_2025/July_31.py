# 898. Bitwise ORs of Subarrays

"""
Given an integer array arr, return the number of distinct bitwise ORs of all the non-empty subarrays of arr.

The bitwise OR of a subarray is the bitwise OR of each integer in the subarray. The bitwise OR of a subarray of one integer is that integer.

A subarray is a contiguous non-empty sequence of elements within an array.

Example :

Input: arr = [0]
Output: 1
Explanation: There is only one possible result: 0.
"""

from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        cur = set()
        for num in arr:
            new_cur = {num}
            for x in cur:
                new_cur.add(x | num)
            res.update(new_cur)
            cur = new_cur
        return len(res)

s = Solution()
print(s.subarrayBitwiseORs([1, 2, 4]))  #output: 6