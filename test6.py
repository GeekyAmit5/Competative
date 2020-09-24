#not complete

def isInfinite(x):
    while x:
        if (x % 10) % 2:
            return False
        x //= 10
    return True


def findUpper(x):
    s = str(x)
    ns = ''
    t = True
    for i in s:
        if t and int(i) % 2:
            ns += str(int(i)+1)
            t = False
        else:
            if not t:
                ns += '0'
            else:
                ns += i
    return int(ns)


def findLower(x):
    s = str(x)
    ns = ''
    t = True
    for i in reversed(s):
        if t and int(i) % 2:
            ns += str(int(i)-1)
            t = False
        else:
            if not t:
                ns += '0'
            else:
                ns += i
    return int(ns)


def gcd(x, y):
    if y:
        return gcd(y, x % y)
    return x


t = int(input())
for i in range(t):
    n = int(input())
    if isInfinite(n):
        print('Unlimited Power')
    else:
        x = findUpper(n)
        y = findLower(n)
        print(x, y)
        # y = find(n, -1)
        # d = gcd(x-n, n-y)
        # x = (x-n)//d
        # y = (n-y)//d
        # print('{}/{}'.format(x, y))
