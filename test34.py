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
        if self.parent:
            return 1 + self.parent.get_level()
        return 0


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
