import random
import numpy as np
import time


def solve(a):
    n = len(a)
    m = len(a[0])
    visited = set()
    for i in range(m):
        x, y = 0, i
        while (x, y) not in visited and 0 <= x < n and 0 <= y < m:
            visited.add((x, y))
            if a[x][y] == 1:
                y -= 1
            elif a[x][y] == 2:
                y += 1
            elif a[x][y] == 3:
                x -= 1
            else:
                x += 1
    return n*m - len(visited)


n, m = random.randint(1, 1000), random.randint(1, 1000)
a = [[random.randint(1, 4) for i in range(m)] for j in range(n)]
# print(np.matrix(a))
# print(n, m)
t0 = time.time()
print(solve(a))
t1 = time.time()
print('Time:', t1-t0)
