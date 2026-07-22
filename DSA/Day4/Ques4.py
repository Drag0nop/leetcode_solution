# Combinations Sum 1: Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers sum to target. 
# You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency
# of at least one of the chosen numbers is different.

def combinationSum(candidates, target):
    res = []
    comb = []

    def backtrack(path, target):
        if target == 0:
            res.append(comb[:])
            return
        if target < 0:
            return

        for i in range(path, len(candidates)):
            comb.append(candidates[i])
            backtrack(i, target - candidates[i])
            comb.pop()
    
    backtrack(0, target)
    return res

# Example usage:
candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))