class graph:
    def __init__(self) -> None:
        self.graph = dict()

    def createVertex(self, a):
        self.graph[a] = set()

    def insert(self, a, b):
        self.graph[a].add(b)
        self.graph[b].add(a)

    def remove(self, a, b):
        self.graph[a].remove(b)
        self.graph[b].remove(a)

    def destroy(self, a):
        del self.graph[a]
        for k in self.graph:
            if a in self.graph[k]:
                self.graph[k].remove(a)


g = graph()
for _ in range(int(input())):
    entrada = input().split()
    if entrada[0] == 'IV':
        vertex = entrada[1]
        g.createVertex(vertex)
    elif entrada[0] == 'IA':
        vertex1, vertex2 = entrada[1], entrada[2]
        if vertex1 in g.graph and vertex2 in g.graph:
            g.insert(vertex1, vertex2)
    elif entrada[0] == 'RV':
        vertex = entrada[1]
        if vertex in g.graph:
            g.destroy(vertex)
    elif entrada[0] == 'RA':
        vertex1, vertex2 = entrada[1], entrada[2]
        if vertex1 in g.graph and vertex2 in g.graph and vertex1 in g.graph[vertex2] and vertex2 in g.graph[vertex1]:
            g.remove(vertex1, vertex2)
min = None
for k in g.graph:
    l = len(g.graph[k])
    if min is None: min = l
    else:
        if l < min:
            min = l
if g.graph == dict():
    print(0)
else: print(min)
