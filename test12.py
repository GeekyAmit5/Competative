import random as rd
import numpy as np


def det(l):
    n = len(l)
    if n == 1:
        return l[0][0]
    else:
        s = 0
        for i in range(n):
            a = [[l[j][k] for k in range(1, n)] for j in range(n) if j != i]
            s += pow(-1, i) * l[0][i] * det(a)
        return s


n = 3
a = [[rd.randint(-10, 10) for i in range(3)] for j in range(3)]
print(np.matrix(a))
for i in range(n):
    ans = [[a[k][j] for k in range(n) if k != i] for j in range(1, n)]
    print('\n', np.matrix(ans))
