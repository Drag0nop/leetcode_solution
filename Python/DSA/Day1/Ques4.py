# Container with most Water - You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]). 
# Find two lines that together with the x-axis form a container, such that the container contains the most water(depth is constant across containers). 
# Return the area(that the 2 lines and the X axis make) of container which can store the max amount of water. 
# Notice that you may not slant the container.

def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        current_area = width * (min(height[left], height[right]))
        max_area = max(max_area, current_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# Example usage:
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))  # Output: 49