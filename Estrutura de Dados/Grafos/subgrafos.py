from collections import defaultdict

class graph():
    # directed graph
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def insert(self, a, b):
        self.graph[a].extend(b)

def isSub(g2,g1):
    for k in g2.graph:
        for v in g2.graph[k]:
            if v not in g1.graph[k]:
                return False
    return True

g1 = graph()
g2 = graph()
for _ in range(int(input())):
    adjs = []
    entrada = list(map(int, input().split()))
    key = entrada.pop(0)
    if int(entrada[0]) > 0:
        entrada.pop(0)
        adjs = entrada
    g1.insert(key, adjs)
input()
for _ in range(int(input())):
    entrada = list(map(int, input().split()))
    key = entrada.pop(0)
    if int(entrada[0]) > 0:
        entrada.pop(0)
        adjs = entrada
        g2.insert(key, adjs)

if (g2.graph == defaultdict(list)) or isSub(g2, g1):
    print('Sub-sub!')
else: print('Ue? Ue? Ue?')