n = int(input())
ans = n//10
n -= 10*ans
ans += n//5
n -= 5*(n//5)
ans += n
print(ans)
