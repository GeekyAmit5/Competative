import time


def slow(n):
    p = [i for i in range(2, n+1)]
    i = 0
    while True:
        t = p[i]*p[i]
        if t > n:
            return p
        while t <= n:
            if t in p:
                p.remove(t)
            t += p[i]
        i += 1


def isPrime(n):
    if n <= 1 or (n > 2 and not n % 2):
        return False
    elif n == 2:
        return True
    for i in range(3, int(n**0.5)+1, 2):
        if not n % i:
            return False
    return True


def fast(n):
    p = []
    for i in range(2, n+1):
        if isPrime(i):
            p.append(i)
    return p


n = int(input())
t0 = time.time()
# slow(n)
fast(n)
t1 = time.time()
print(t1-t0)
