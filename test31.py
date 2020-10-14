def fact(n):
    if n <= 1:
        return 1
    return n*fact(n-1)


t = int(input())
for i in range(t):
    l, r = map(int, input().split())
    c = 0
    for j in range(l, r+1):
        if not fact(j-1) % j:
            c += 1
    print(c)
