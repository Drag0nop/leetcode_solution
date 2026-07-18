# Josephus problem: There are n friends that are playing a game. 
# The friends are sitting in a circle and are numbered from 1 to n in clockwise order. 
# More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and 
# moving clockwise from the nth friend brings you to the 1st friend.

# The rules of the game are as follows:
# 1.Start at the 1st friend.
# 2.Count the next k friends in the clockwise direction including the friend you started at. 
# The counting wraps around the circle and may count some friends more than once.

# 3.The last friend you counted leaves the circle and loses the game.
# 4.If there is still more than one friend in the circle, 
# go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.

# 5.Else, the last friend in the circle wins the game.

# Given the number of friends, n, and an integer k, return the winner of the game.

# Type 1: Using recursion:
def josephus(n, k):
    if n == 1:
        return 1
    return (josephus(n - 1, k) + k - 1) % n + 1

# Type 2: Using iteration:
def josephus(n, k):
    res = 0
    for i in range(2, n + 1):
        res = (res + k) % i
    return res + 1

# Type 3: Using list to simulate the process:
def josephus(n, k):
    res = [i for i in range(1, n + 1)]
    temp = 0
    while len(res) != 1:
        num = (temp + k - 1) % len(res)
        res.pop(num)
        temp = num
    return res[0]


# Example usage:
n = 5
k = 2
print(josephus(n, k))  # Output: 3 