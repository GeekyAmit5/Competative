def gcd(x, y):
    if y:
        return gcd(y, x % y)
    return x


a, b = map(int, input().split())
print(gcd(a, b))
