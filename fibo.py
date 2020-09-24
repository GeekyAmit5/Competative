def fibo(n):
    ans = 0
    a = 1
    b = 1
    for i in range(n):
        ans = a+b
        b = a % 10
        a = ans % 10
    return ans


a, b = map(int, input().split())
ans = (fibo(a)**2+fibo(b)**2) % 10
print(ans)
