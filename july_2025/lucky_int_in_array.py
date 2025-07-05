"""
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.
Return the largest lucky integer in the array. If there is no lucky integer return -1.

Example 1:

Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
"""

from typing import List

# not a very much good approach(cause the complexity will be O(n^2)), the Counter-based approach is is better(O(n) complexity)
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr1 = []
        for i in range(len(arr)):
            cnt = 0
            k = arr[i]
            for j in range(len(arr)):
                if arr[j] == k:
                    cnt += 1
            if k == cnt:
                arr1.append(k)
        if len(arr1) == 0:
            return -1
        else:
            return max(arr1)

s = Solution()
print(s.findLucky([2,2,3,4]))