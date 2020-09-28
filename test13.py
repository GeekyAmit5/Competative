import numpy as np

n = int(input())
a = np.zeros((n, n), dtype=int)
num = 1
l = 0
while num <= n*n:
    for i in range(n):
        if not a[l][i]:
            a[l][i] = num
            num += 1
    for i in range(n):
        if not a[i][n-1-l]:
            a[i][n-1-l] = num
            num += 1
    for i in range(n):
        if not a[n-1-l][n-1-i]:
            a[n-1-l][n-1-i] = num
            num += 1
    for i in range(n):
        if not a[n-1-i][l]:
            a[n-1-i][l] = num
            num += 1
    l += 1

print(np.matrix(a))
