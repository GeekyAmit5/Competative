def solve():
    global ans, d
    if d == n:
        val = ''.join(ans)
        if val not in all:
            all.append(val)
            print(val)
    else:
        for i in s:
            if ans.count(i) < counts[i]:
                ans.append(i)
                d += 1
                solve()
                d -= 1
                ans.pop()


s = 'lmao6756'
counts = {}
for i in s:
    counts[i] = counts.get(i, 0) + 1
n = len(s)
ans, d, all = [], 0, []
solve()
print('Total:', len(all))
