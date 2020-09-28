def solve():
    global ans, total
    if len(ans) == 16:
        print(''.join(ans))
        total += 1
    else:
        for i in ['r', 'u']:
            if ans.count(i) < 8:
                ans.append(i)
                solve()
                ans.pop()


total = 0
ans = []
solve()
print('Total:', total)
