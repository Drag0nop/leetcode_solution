# Subsets 2: Given an integer array nums that may contain duplicates, 
# return all possible subsets (the power set). 
# The solution set must not contain duplicate subsets. 
# Return the solution in any order.

def subsetsWithDup(nums):
    nums.sort()
    res = []
    subset = []

    def backtrack(path):
        if path == len(nums):
            res.append(subset[:])
            return
        
        subset.append(nums[path])
        backtrack(path + 1)
        subset.pop()
        while path + 1 < len(nums) and nums[path] == nums[path + 1]:
            path += 1
        backtrack(path + 1)

    backtrack(0)
    return res

# Example usage:
nums = [1, 2, 2]
print(subsetsWithDup(nums))