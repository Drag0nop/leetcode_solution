# 01 Knapsack: You are provided with a set of N items, each with a specified weight and value. 
# Your objective is to pack these items into a backpack with a weight limit of W, 
# maximizing the total value of items in the backpack. 
# Specifically, you have two arrays: val[0..N-1], representing the values of the items, and 
# wt[0..N-1], indicating their weights. 
# Additionally, you have a weight limit W for the backpack. 
# The challenge is to determine the most valuable combination of items where the total weight does not exceed W. 
# Note that each item is unique and indivisible, meaning it must be either taken as a whole or left entirely.

def knapsack(N, W, values, weights):
    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(W + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[N][W]

# Example Usage:
N = 3
W = 8
values = [2, 3, 9]
weights = [8, 2, 5]
print(knapsack(N, W, values, weights))

