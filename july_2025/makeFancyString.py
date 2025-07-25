"""
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.

Example :

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
"""

class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        count = 0
        
        for char in s:
            if not result or result[-1] != char:
                count = 1
                result.append(char)
            elif count < 2:
                count += 1
                result.append(char)
        
        return ''.join(result)

s = Solution()
print(s.makeFancyString("leeetcode"))  # Output: "leetcode"