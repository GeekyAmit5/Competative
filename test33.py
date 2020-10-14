import random
import numpy as np


def c(x):
    t = 0
    for i in range(7):
        t += ans[i].count(x)
        if t >= 3:
            break
    return t


def isValid(job, i):
    if (i == 0 or job not in ans[i-1]) and job not in ans[i]:
        if job == 'Free' and c(job) == 0:
            return True
        if job != 'Free' and c(job) < 3:
            return True
    return False


def solve():
    global ans, depth
    for i in range(7):
        for j in range(4):
            if not ans[i][j]:
                for job in jobs:
                    if isValid(job, i):
                        ans[i][j] = job
                        solve()
                        ans[i][j] = 0
                return
    print(np.matrix(ans))
    exit()


jobs = ['GT', 'FSaA', 'Coding', 'PaS', 'PDE',
        'RoFG', 'FA', 'BA', 'NET/GATE', 'Free']
random.shuffle(jobs)
ans = [[0 for i in range(4)] for j in range(7)]
solve()
