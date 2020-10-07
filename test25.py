t = int(input())
for i in range(t):
    e, n = map(int, input().split())
    m = [[0 for i in range(n)] for j in range(n)]
    for j in range(e):
        a, b, c = map(int, input().split())
        m[a-1][b-1] = m[b-1][a-1] = c
    q = [0]
    while len(q) != n:
        b = [i for i in range(n) if i not in q]
        mx = m[q[-1]].index(max(m[q[-1]]))
        q.append(mx)
    mx = 0
    for i in range(n-1):
        mx += m[q[i]][q[i+1]]
    print(mx)
