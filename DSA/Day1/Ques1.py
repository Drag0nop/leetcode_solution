# Sorted Squared Array - You are given an array of Integers in which each subsequent value is not less than the previous value. 
# Write a function that takes this array as an input and returns a new array with the squares of each number sorted in ascending order.

def sorted_squared_array(arr):
    res = [0] * len(arr)
    if len(arr) == 0: return res
    left, right = 0, len(arr) - 1
    while left <= right:
        left_square = arr[left] ** 2
        right_square = arr[right] ** 2
        if left_square > right_square:
            res[right - left] = left_square
            left += 1
        else:
            res[right - left] = right_square
            right -= 1
    return res

# Example usage:
input_array = [-4, -1, 0, 3, 10]
print(sorted_squared_array(input_array))