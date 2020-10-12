
from collections import deque


def isPrime(x):
    if x == 2:
        return True
    elif x <= 1 or x % 2 == 0:
        return False
    else:
        for i in range(3, int(x**0.5)+1, 2):
            if x % i == 0:
                return False
    return True


def isValid(x):
    if ans and isPrime(ans[0]):
        return True
    elif sum(ans) + x <= 4:
        return True
    elif not ans and isPrime(x):
        return True
    return False


def solve():
    global ans, all
    if len(ans) == 3:
        all.add(tuple(ans))
    else:
        for i in [x for x in range(1, 7)]:
            if isValid(i):
                ans.append(i)
                solve()
                ans.pop()


ans = deque()
all = set()
solve()
print(all)
print('Total:', len(all))

# n = 3
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         for k in range(1, n+1):
#             ans = (i, j, k)
#             print(ans)
