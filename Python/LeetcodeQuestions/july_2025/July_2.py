# 3333. Find the Original Typed String II

"""
Alice is attempting to type a specific string on her computer. However, 
she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.
You are given a string word, which represents the final output displayed on Alice's screen. You are also given a positive integer k.
Return the total number of possible original strings that Alice might have intended to type, if she was trying to type a string of size at least k.

Since the answer may be very large, return it modulo 109 + 7.

Example 1:

Input: word = "aabbccdd", k = 7
Output: 5

Explanation:
The possible strings are: "aabbccdd", "aabbccd", "aabbcdd", "aabccdd", and "abbccdd".
"""

# DP (Dynamic Programming): Used to count the number of possible "invalid" strings with length < k.
# Prefix sums: Used to speed up DP transition via cumulative sums.
# Group Compression: Count how many identical characters are in each consecutive group (aaa, bbb, etc.)

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        res = cnt = 1   # res -> multiplicative result
        MOD = 10**9 + 7   # avoid integer overflow
        groups = []
        for i in range(1,len(word)):
            if word[i] == word[i-1]: cnt+=1
            else:
                groups.append(cnt)
                res = (res * cnt)%MOD
                cnt = 1
        groups.append(cnt)
        res = (res * cnt)%MOD
        if k<=len(groups): return res

        prev = [0]*k
        prev[0] = 1

        for i in range(1,len(groups)+1):
            curr = [0]*k
            currSum = 0
            for j in range(1,k):   # main DP transition which uses sliding window prefix sum optimization
                currSum = (currSum + prev[j-1]-(prev[j-1-groups[i-1]] if j-1-groups[i-1]>=0 else 0))%MOD
                curr[j] = currSum    
            prev = curr    
        
        prevSum = 0
        for num in prev: prevSum = (prevSum + num)%MOD
        return (res - prevSum + MOD)%MOD


s = Solution()
print(s.possibleStringCount("aaabbb", 3))  # Output: 8