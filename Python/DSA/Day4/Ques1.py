# Subsets: Given an integer array of unique elements, return all possible subsets (the power set). 
# The solution set must not contain duplicate subsets. Return the solution in any order.

def subsets(nums):
    res = []
    subset = []
    def backtrack(path):
        if path == len(nums):
            res.append(subset[:])
            return
        
        subset.append(nums[path])
        backtrack(path + 1)

        subset.pop()
        backtrack(path + 1)
    
    backtrack(0)
    return res

# Example usage:
nums = [1, 2, 3]
print(subsets(nums))