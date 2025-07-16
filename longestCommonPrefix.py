"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example :

Input: strs = ["flower","flow","flight"]
Output: "fl"
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in strs[1:]:
                if i >= len(j) or j[i] != char:
                    return strs[0][:i]
        return strs[0]

s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))  # output "