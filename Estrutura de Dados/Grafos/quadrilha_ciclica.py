from collections import defaultdict

class graph():
    # directed graph
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def insert(self, a, b):
        self.graph[a].extend(b)

    def ciclic(self, explored=None, start=None):
        if not explored:
            start = [i for i in self.graph][0]
            explored = set()
            explored.add(start)
        for i in self.graph[start]:
            if i not in explored:
                explored.add(i)
                return self.ciclic(explored, i)
            else:
                return True
        return False

g = graph()
for _ in range(int(input())):
    adjs = []
    entrada = input().split()
    key = entrada.pop(0)
    if int(entrada[0]) > 0:
        entrada.pop(0)
        adjs = entrada
    g.insert(key, adjs)

if g.ciclic():
    print('Hoje tem!')
else:
    print('... que ama ninguem.')


