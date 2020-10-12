
def fact(x):
    if x <= 1:
        return 1
    return x*fact(x-1)


def C(n, r):
    return fact(n) // (fact(n-r)*fact(r))


ans = 1
f = 52
for i in range(4):
    ans *= C(f, 13)
    f -= 13
print(ans)

if ans == fact(52) // fact(13)**4:
    print('Well Done!')
else:
    print('Very Bad!')
