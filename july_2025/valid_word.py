"""
A word is considered valid if:

It contains a minimum of 3 characters.
It contains only digits (0-9), and English letters (uppercase and lowercase).
It includes at least one vowel.
It includes at least one consonant.
You are given a string word.

Return true if word is valid, otherwise, return false.

Notes:

'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
A consonant is an English letter that is not a vowel.
 

Example :

Input: word = "234Adas"
Output: true

Explanation:

This word satisfies the conditions.
"""

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        vowels = "aeiouAEIOU"
        cnt = False
        n = False
        for j in word:
            if j.isdigit():
                continue
            elif j.isalpha():
                if j in vowels:
                    cnt = True
                else:
                    n = True
            else:
                return False
        
        return cnt and n

s = Solution()
print(s.isValid("aya"))  # Output: True