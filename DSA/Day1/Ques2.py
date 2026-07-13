#  Monotonic Array - An array is monotonic if it is either monotone increasing or monotone decreasing. 
# An array is monotone increasing if all its elements from left to right are non-decreasing. An array is monotone decreasing if all  its elements from left to right are non-increasing. 
# Given an integer array return true if the given array is monotonic, or false otherwise.

def is_monotonic(arr):
    n = len(arr)
    if n <= 1: return True

    for i in range(1, n):
        if arr[i] < arr[i - 1]: break
        if i == n - 1: return True
    
    for i in range(1, n):
        if arr[i] > arr[i - 1]: break
        if i == n - 1: return True

    return False

# Example usage:
input_array = [1, 2, 2, 3]
print(is_monotonic(input_array))