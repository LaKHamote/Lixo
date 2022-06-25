from collections import defaultdict

class graph():
    # directed graph
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def insert(self, a, b):
        self.graph[a].extend(b)

def provAmigos(g):
    conhecidos = []
    amigos = g.graph['Mussum']
    g.graph['Mussum'] = [] 
    count = 0
    for k in g.graph:
        for v in g.graph[k]:
            if v in amigos:
                count += 1
            if count >= 3 and k not in amigos:
                conhecidos.append(k)
                break
        count = 0
    return conhecidos




g = graph()
for _ in range(int(input())):
    adjs = []
    entrada = input().split()
    key = entrada.pop(0)
    if int(entrada[0]) > 0:
        entrada.pop(0)
        adjs = entrada
    g.insert(key, adjs)

conhecidos = sorted(provAmigos(g))
if conhecidos:
    print(*conhecidos, sep='\n')
else:
    print('Cacildis! Cade elis?')