def solve():
    global mn, ans
    if ans[-1] == a:
        c = 0
        for i in range(len(ans)-1):
            c += adj[ans[i]][ans[i+1]]
        mn = min(c, mn)
    else:
        for i in range(n):
            if adj[ans[-1]][i] and i not in ans:
                ans.append(i)
                solve()
                ans.pop()


t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    adj = [[0 for i in range(n)] for i in range(n)]
    for j in range(m):
        x, y, c = map(int, input().split())
        adj[x-1][y-1] = adj[y-1][x-1] = c
    q = int(input())
    for g in range(q):
        a, k = map(int, input().split())
        a -= 1
        mn = k
        ans = [0]
        solve()
        print(max(0, k-2*mn))
