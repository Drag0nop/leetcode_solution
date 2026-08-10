# Tribonacci: The Tribonacci sequence Tn is defined as follows:

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

def Tribonacci(n):
    a, b, c = 0, 1, 1
    if n <= 1: return n
    if n == 2: return c

    for i in range(3, n + 1):
        a, b, c = b, c, a + b + c

    return c

# Example Usage:
print(Tribonacci(4))