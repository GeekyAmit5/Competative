def isGraphical(s):
    s.sort(reverse=True)
    print(s)
    if len([i for i in s if i % 2]) % 2 or min(s) < 0 or max(s) > len(s)-1 or (len(s) == 1 and s[0] != 0):
        return False
    elif max(s) <= 1:
        return True
    return isGraphical([s[i]-1 for i in range(1, s[0]+1)]+s[s[0]+1:])


s = list(map(int, input('Enter degree sequence: ').split()))
if isGraphical(s):
    print('Graphical')
else:
    print('Not Graphical')
