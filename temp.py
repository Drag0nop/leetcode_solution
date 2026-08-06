def func(n, L, C):
    max0 = second0 = float('-inf')
    max1 = second1 = float('-inf')

    for val, col in zip(L, C):

        if col == 0:
            if val >= max0:
                second0 = max0
                max0 = val
            elif val > second0:
                second0 = val

        else:
            if val >= max1:
                second1 = max1
                max1 = val
            elif val > second1:
                second1 = val

    ans = 0

    if second0 != float('-inf'):
        ans = max(ans, max0 + second0)

    if second1 != float('-inf'):
        ans = max(ans, max1 + second1)

    return ans

# n = 4
# L = [10, 20, 30, 40]
# C = [0 ,0, 1, 1]
# print(func(n, L, C))    output: 70
n = 3
L = [100, 10, 50]
C = [1, 1, 1]
print(func(n, L, C)) #output: 150

