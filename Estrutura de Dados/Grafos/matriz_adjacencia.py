class graph():
    def __init__(self, n) -> None:
        self.graph = [[f'{0:3}' for _ in range(n)] for _ in range(n)]

    def show(self):
        for i in self.graph:
            print(' ',end='')
            print(*i)

    def directed_insert(self, i, j, p):
        self.graph[i][j] = f'{p:3}'
    
    def undirected_insert(self, i, j, p):
        self.graph[i][j] = f'{p:3}'
        self.graph[j][i] = f'{p:3}'

v, a, tipo = input().split()
g = graph(int(v))
if tipo == 'D':
    for _ in range(int(a)):
        l, c, p = map(int, input().split())
        g.directed_insert(l-1, c-1, p)

if tipo == 'N':
    for _ in range(int(a)):
        l, c, p = map(int, input().split())
        g.undirected_insert(l-1, c-1, p)

g.show()