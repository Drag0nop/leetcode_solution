# Combinations Sum 2: Given a collection of candidate numbers (candidates) and a target number (target), 
# find all unique combinations in candidates where the candidate numbers sum to target. 
# Each number in candidates may only be used once in the combination. 
# Note: The solution set must not contain duplicate combinations.

def combinationSum2(candidates, target):
    candidates.sort()
    res = []

    def backtrack(target, path, comb):
        if target == 0:
            res.append(comb)
            return
        if target < 0:
            return

        for i in range(path, len(candidates)):
            if i > path and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            backtrack(target - candidates[i], i + 1, comb + [candidates[i]])
    backtrack(target, 0, [])
    return res

# Example usage:
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combinationSum2(candidates, target))