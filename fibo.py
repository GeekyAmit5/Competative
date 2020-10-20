m, n = map(int, input().split())
if n <= 2:
    print(1)
    exit()
a = 1
b = 1
for i in range(m, n-2):
    a, b = b, a+b
print(b)
