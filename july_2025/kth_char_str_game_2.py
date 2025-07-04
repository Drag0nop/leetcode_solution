"""
Alice and Bob are playing a game. Initially, Alice has a string word = "a".
You are given a positive integer k. You are also given an integer array operations, where operations[i] represents the type of the ith operation.
Now Bob will ask Alice to perform all operations in sequence:
▬ If operations[i] == 0, append a copy of word to itself.
▬ If operations[i] == 1, generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word. For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".
Return the value of the kth character in word after performing all the operations.
Note that the character 'z' can be changed to 'a' in the second type of operation.

Example 1:

Input: k = 5, operations = [0,0,0]
Output: "a"

Explanation:

Initially, word == "a". Alice performs the three operations as follows:

Appends "a" to "a", word becomes "aa".
Appends "aa" to "aa", word becomes "aaaa".
Appends "aaaa" to "aaaa", word becomes "aaaaaaaa".
"""

from typing import List

# 0ms  of runtime
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        k -= 1
        bits = k.bit_length()
        res = 0
        for i in range(bits):
            if (k >> i) & 1:
                res += operations[i]
        return chr(ord('a') + (res % 26))


# also can be written it llike this too.(2ms of runtime)
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        k -= 1
        num = k
        bits = 0
        while num:
            num = num//2
            bits += 1
        res = 0
        for i in range(bits):
            if (k >> i) & 1:
                res += operations[i]
        return chr(ord('a') + (res % 26))



s = Solution()
print(s.kthCharacter(5,[0,0,0]))