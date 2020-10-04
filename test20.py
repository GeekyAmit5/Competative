import numpy as np
import random


def det(m):
    n = len(m)
    if n == 1:
        return m[0][0]
    s = 0
    for k in range(n):
        s += pow(-1, k) * m[0][k] * det([[m[j][i]
                                          for i in range(n) if i != k] for j in range(1, n)])
    return s


n = random.randint(1, 5)
a = [[random.randint(-10, 10) for i in range(n)] for j in range(n)]
print(np.matrix(a))
print('Determinant:', det(a))
