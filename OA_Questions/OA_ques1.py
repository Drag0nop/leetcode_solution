# You are given an array of N integers and need to select exactly P pairs of elements from this array. 
# Each element can be used in at most one pair. 
# Your goal is to minimize the maximum absolute difference among all selected pairs.

# The difference of a pair consisting of elements at positions i and j 2026-0 is defined as (arr[i] - arr[j]). 
# Among all valid ways to form P pairs, you must find the arrangement where the largest difference across all pairs is as small as possible. 
# If P is 0, return 0.

# ================Function Description================:
# Complete the function findMinMaxDifference in the editor.

# ================Parameters================:
# int N: the size of the array
# int P: the number of pairs pairs to form
# int arr[N]: the array elements

# ================Returns================:
# int: the minimum possible value of the maximum difference among all P pairs

# ================Input Format================:
# The first line contains a single integer N, the number of elements in the array.
# The second line contains a single integer P, the number of pairs to form.
# The third line contains N space-separated integers representing the array elements.

# ================Output Format================:
# Print a single integer the minimum value of the maximum difference achievable when forming P pairs optimally.

# ================Constraints================
# 1 <= N <= 10 ^ 5
# 0 <= P <= N / 2
# 0 <= arr[i] <= 10 ^ 9

# =============================================================================

# This problem is solved using Binary Search + Greedy.

# Idea
# Sort the array.
# Suppose the maximum allowed difference is x.
# Check whether it is possible to form at least P pairs such that every pair has difference <= x.
# Use binary search on the answer.

# Time Complexity
# Sorting: O(N log N)
# Binary Search: O(log(max(arr)-min(arr)))
# Checking feasibility: O(N)

def findMinMaxDifference(N, P, arr):
    if P == 0:
        return 0

    arr.sort()

    def can_form(max_diff):
        pairs = 0
        i = 0

        while i < N - 1:
            if arr[i + 1] - arr[i] <= max_diff:
                pairs += 1
                i += 2  # use both elements
            else:
                i += 1

            if pairs >= P:
                return True

        return False

    left = 0
    right = arr[-1] - arr[0]
    ans = right

    while left <= right:
        mid = (left + right) // 2

        if can_form(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


# Input
N = int(input())
P = int(input())
arr = list(map(int, input().split()))

print(findMinMaxDifference(N, P, arr))

# Sample Input 1                    |    Sample Output 1
# 6                                 |    1
# 2                                 |
# 10 1 2 7 1 3                      |


# Explanation
# The input array is [10, 1, 2, 7, 1, 3] and we need to form 2 pairs.
# After sorting: [1, 1, 2, 3, 7, 10]
# First pair: elements 1 and 1, difference = 0
# Second pair: elements 2 and 3, difference = 1
# Maximum difference among the pairs max(0, 1) = 1
# This is optimal as no other pairing strategy can achieve a smaller maximum difference.