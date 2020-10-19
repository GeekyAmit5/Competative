import random
from time import time
from math import inf


def solve(s, k):
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i+k, n+1, k):
            temp = set(s[i:j])
            for x in temp:
                if s[i:j].count(x) != k:
                    break
            else:
                # print(s[i:j])
                ans += 1
    return ans


i = 0
mx = 0
while i < 1000:
    s = str(random.randint(1, 10**10000))
    k = random.randint(1, 10**5)
    # print(s, k)
    t0 = time()
    solve(s, k)
    t1 = time()
    mx = max(mx, t1-t0)
    print('After', i, 'iterations maximum is', mx)
    if mx > 5:
        break
    i += 1
print('Maximum Time:', mx)
