# Combinations: Given two integers n and k, 
# return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

def combine(n, k):
    res = []
    comb = []

    def backtrack(path):
        if len(comb) == k:
            res.append(comb[:])
            return

        need = k - len(comb) 
        for i in range(path, n - (need - 1) + 1):
            comb.append(i)
            backtrack(i + 1)
            comb.pop()
    
    backtrack(1)
    return res

# Example usage:
n = 4
k = 2
print(combine(n, k))