def isvalid(c):
    if c == 'b':
        if color and len(color) < n-1:
            return True
        return False
    else:
        if color and color[-1] == c:
            return False
        return True


def solve():
    global color, ans
    if len(color) == n:
        print(color)
        ans += 1
    else:
        for i in colors:
            if isvalid(i):
                color.append(i)
                if i == 'b':
                    if color[-2] == 'r':
                        color.append('w')
                    else:
                        color.append('r')
                solve()
                color.pop()
                if color and color[-1] == 'b':
                    color.pop()


colors = ['r', 'w', 'b']
t = int(input())
for i in range(t):
    n = int(input())
    color = []
    ans = 0
    solve()
    print('Total:', ans)
