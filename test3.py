def solve():
    global ans, total
    if len(ans) == k:
        total += 1
    else:
        for i in ['h', 'e']:
            if i == 'h' or not ans or ans[-1] == 'h':
                ans.append(i)
                solve()
                ans.pop()


t = int(input())
d = {1: 2, 2: 5, 3: 10}
for i in range(t):
    n = int(input())
    for i in range(1, n+1):
        if i not in d:
            k = i
            total = 0
            ans = []
            solve()
            d[i] = d[i-1] + total
    print(d)
