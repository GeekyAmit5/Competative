def redump(l):
    if len(l) == len(set(l)):
        return l
    else:
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                if l[i] == l[j]:
                    l.pop(j)
                    return redump(l)


l = [3, 1, 3, 5, 6, 7, 8, 6, 3]
print(redump(l))
