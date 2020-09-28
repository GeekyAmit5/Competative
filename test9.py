n, h = map(int, input().split())
a = list(map(int, input().split()))
c = 0
i = 1

while c < h:
    c += a[(i-1) % n]
    h -= i
    i += 1
print(i-1)
