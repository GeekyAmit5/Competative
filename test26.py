
def solve():
    global ans, t
    if 'DD' in ans or len(ans) == 4:
        print(ans)
        t += 1
    else:
        for i in ['D', 'N']:
            ans += i
            solve()
            ans = ans[:-1]


ans, t = '', 0
solve()
print('Total:', t)
