from collections import deque


class node():
    def __init__(self, num):
        self.num = num
        self.parent = None
        self.child = []

    def add_child(self, num):
        self.child.append(num)
        num.parent = self

    def get_level(self):
        level = 0
        temp = self.parent
        while temp:
            level += 1
            temp = temp.parent
        return level


def Tree(root):
    q = deque([root])
    while q:
        p = q[0]
        q.popleft()
        for i in adjList[p]:
            if nodes[p].parent != nodes[i] and nodes[i] not in nodes[p].child:
                nodes[p].add_child(nodes[i])
                q.append(i)


n, m = map(int, input().split())
nodes = [node(i) for i in range(n)]
adjList = [set() for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    adjList[a-1].add(b-1)
    adjList[b-1].add(a-1)
Tree(0)
for i in nodes:
    print('vertex:', i.num+1)
    if i.parent:
        print('Parent:', i.parent.num+1)
    else:
        print('Parent:', i.parent)
    print('Childs:', end='\t')
    for j in i.child:
        print(j.num+1, end='\t')
    print('\n')
