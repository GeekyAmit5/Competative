from functools import lru_cache
import sys

sys.setrecursionlimit(10**5)

c = dict()


def C(n, r):
    if r == n or r == 0:
        return 1
    else:
        ans = C(n-1, r) + C(n-1, r-1)
        c[(n, r)] = ans
        c[(n, n-r)] = ans
        return ans


n, r = map(int, input().split())
if r > n:
    print(r, 'is greater than', n)
else:
    print(C(n, r))
