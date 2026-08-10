# Leetcode Question No. 167 -> Two Sum II - Input Array Is Sorted
# Complexity Analysis:
# Time Complexity: O(N), where N is the number of elements in the array.

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while  i < j:
            k = numbers[i] + numbers[j]
            if k == target:
                return [i + 1,j + 1]
            elif k < target:
                i += 1
            else:
                j -= 1

s = Solution()
print(s.twoSum([2,7,11,15], 9)) #output: [1, 2]