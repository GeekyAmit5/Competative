t = int(input())
for i in range(t):
    s = input()
    c = 0
    l = ''
    for i in s:
        if i in 'ABCabc':
            l += i
        else:
            n = len(l)
            c += n*(n+1)//2
            l = ''
    n = len(l)
    c += n*(n+1)//2
    print(c)
