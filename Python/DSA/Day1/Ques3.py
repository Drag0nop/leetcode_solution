# Rotate Array - Given an array, rotate the array to the right by k steps, 
# where k is non-negative.

def rotate(nums, k):
    n = len(nums)
    k = k % n  # In case k is greater than n
    nums[:] = nums[-k:] + nums[:-k]  # Rotate the array in place
    return nums

# Example usage:
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate(nums, k))  # Output: [5, 6, 7, 1, 2, 3, 4]
# time complexity: O(n)
# space complexity: O(1)