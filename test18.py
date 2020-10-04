def div(n):
    ans = {1, n}
    for i in range(2, int(n**0.5)+1):
        if not n % i:
            ans.add(i)
            ans.add(n//i)
    return ans


t = int(input())
for i in range(t):
    n = int(input())
    print(*div(n))
