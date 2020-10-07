# def sub(a):
#     global total
#     if a not in subsets:
#         subsets.append(a)
#         total += 1
#     for i in range(len(a)):
#         b = a[:i] + a[i+1:]
#         sub(b)


# a = ['a', 'b', 'c', 'd']
# subsets = []
# total = 0
# sub(a)
# for i in subsets:
#     print('{'+','.join(i)+'}')
# print('Total:', total)


a = [1, 2, 3, 4, 5]
q = [a]
while q:
    print(q[0])
    for i in range(len(q[0])):
        b = q[0][:i]+q[0][i+1:]
        if b not in q:
            q.append(b)
    q.pop(0)
