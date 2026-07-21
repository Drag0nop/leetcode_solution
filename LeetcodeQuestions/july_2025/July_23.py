# 1717. Maximum Score From Removing Substrings

"""
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

Example :

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
"""

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pair(s, first, second, value):
            stack = []
            score = 0
            for c in s:
                if stack and stack[-1] == first and c == second:
                    stack.pop()
                    score += value
                else:
                    stack.append(c)
            return "".join(stack), score

        # Remove the more valuable pair first
        if x > y:
            s, score1 = remove_pair(s, 'a', 'b', x)
            s, score2 = remove_pair(s, 'b', 'a', y)
        else:
            s, score1 = remove_pair(s, 'b', 'a', y)
            s, score2 = remove_pair(s, 'a', 'b', x)

        return score1 + score2


s = Solution()
print(s.maximumGain("cdbcbbaaabab", 4, 5))  #output: 19