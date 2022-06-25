from collections import defaultdict, deque


class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def bfs(self):
        vertices = [i for i in self.graph]
        queue = deque()
        queue.append(vertices[0])
        explored = set()
        explored.add(vertices[0])
        while queue:
            vertex = queue.popleft()
            print(vertex, end=', ')
            for i in self.graph[vertex]:
                if i not in explored:
                    queue.append(i)
                    explored.add(i)
        print('')

    def dfs(self, explored=None, start=None):
        if not explored:
            start = [i for i in self.graph][0]
            explored = set()
            explored.add(start)
            print(start)
        for i in self.graph[start]:
            if i not in explored:
                print(i)
                explored.add(i)
                self.dfs(explored, i)


gr = Graph()
gr.add_edge(6, 7)
gr.add_edge(7, 8)
gr.add_edge(8, 9)
gr.add_edge(9, 10)
gr.add_edge(1, 80)
gr.add_edge(3, 6)
gr.add_edge(80, 3)
gr.add_edge(1, 2)
gr.dfs()
print('')
gr.bfs()

# Para estudar
# Shortest-path usando BFS
# Algoritmo de Dijkstra para grafos
# Algoritmo de Prim para grafos
# The Word Ladder Problem (pythonds)
# The Knight’s Tour (pythonds)
# Strongly Connected Components (pythonds)
# Basicamente, leia todo o conteúdo do pythonds de grafos.
