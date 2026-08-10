# Permutations 2: Given a collection of numbers, nums, that might contain duplicates, 
# return all possible unique permutations in any order.

def permutations2(nums):
    nums.sort()
    res = []
    used = [False] * len(nums)
    def backtrack(path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False
    backtrack([])
    return res

# Example usage:
nums = [1, 1, 2]
print(permutations2(nums))