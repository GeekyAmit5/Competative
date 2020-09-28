import numpy as np

t = int(input())
for i in range(t):
    a, b, c, k = map(int, input().split())
    l = min(np.roots([a, b, c-k]))
    ans = max(0, int(l)+1)
    print(ans)
