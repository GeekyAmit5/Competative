from collections import deque
# look for activity app


def solve():
    global ans, t
    if 'DD' in ''.join(ans) or len(ans) == 20:
        print(''.join(ans))
        t += 1
    else:
        for i in ['D', 'N']:
            ans.append(i)
            solve()
            ans.pop()


ans, t = deque(), 0
solve()
print('Total:', t)
