# Permutations: Given an array nums of distinct integers, return all the possible permutations. 
# You can return the answer in any order.

def permutations(nums):
    res = []
    def backtrack(path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if nums[i] not in path:
                path.append(nums[i])
                backtrack(path)
                path.pop()
    backtrack([])
    return res

# Example usage:
nums = [1, 2, 3]
print(permutations(nums))