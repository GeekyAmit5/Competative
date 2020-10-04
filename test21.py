import time
import random


def isPrime1(n):
    if n <= 1 or (n > 2 and not n % 2):
        return False
    elif n == 2:
        return True
    for i in range(3, int(n**0.5)+1, 2):
        if not n % i:
            return False
    return True


def isPrime(n):
    if n == 2 or n == 3:
        return True
    elif n <= 1 or (n % 6 != 1 and n % 6 != 5):
        return False
    for i in range(5, int(n**0.5)+1, 2):
        if not n % i:
            return False
    return True


# n = int(input())
# n = random.randint(1, 100000000000000)
n = 4872387843870122369748763242376711172938416916198074460027376941111111133137731
print(n)
t0 = time.time()
print(isPrime(n))
t1 = time.time()
print(isPrime1(n))
t2 = time.time()
print('Time:', t1-t0, t2-t1)
