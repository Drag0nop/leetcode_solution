"""
Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, 
resulting in a character being typed multiple times.
Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.
You are given a string word, which represents the final output displayed on Alice's screen.
Return the total number of possible original strings that Alice might have intended to type.

Example 1:

Input: word = "abbcccc"
Output: 5

Explanation:

The possible strings are: "abbcccc", "abbccc", "abbcc", "abbc", and "abcccc"
"""

# Runtime 42ms
class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
        return count

# =============================================================

# Runtime 19ms(better approach)
class Solution:
    def possibleStringCount(self, word: str) -> int:
        stack = []
        ans = 1 
        for w in word:
            if not stack or (stack and w==stack[-1]):
                stack.append(w)
            else:
                ans+=len(stack)-1
                stack = [w]
        ans+=len(stack)-1
        
        return ans 



s = Solution()
print(s.possibleStringCount("aabbbc"))  # Output: 4