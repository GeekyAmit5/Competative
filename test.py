from math import inf
t = int(input())
for j in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = list(set(a))
    m = inf
    for i in s:
        r = a.count(i)
        if r >= k:
            min = 0
            break
        else:
            d = 1
            b = a[:]
            cost = 0
            while r < k and cost < m:
                if i - d in b or i+d in b:
                    if i - d in b:
                        cost += 3*d
                        r += 1
                        b.remove(i-d)
                        if r >= k or cost >= m:
                            continue
                    if i+d in b:
                        r += 1
                        cost += 5*d
                        b.remove(i+d)
                else:
                    d += 1
            else:
                m = min(m, cost)
    print(m)
