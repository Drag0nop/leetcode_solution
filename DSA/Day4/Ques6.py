# Combinations Sum 3: Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
# • Only numbers 1 through 9 are used.
# • Each number is used at most once.

# Return a list of all possible valid combinations. 
# The list must not contain the same combination twice, and the combinations may be returned in any order.

def combinationSum3(k, n):
    res = []
    path = []
    def backtrack(i, n, k):
        if k == 0 and n == 0:
            res.append(path[:])
            return

        for i in range(i, 10):
            if i > n or k <= 0:
                break
            path.append(i)
            backtrack(i + 1, n - i, k - 1)
            path.pop()

    backtrack(1, n, k)
    return res

# Example usage:
k = 3
n = 7
print(combinationSum3(k, n))