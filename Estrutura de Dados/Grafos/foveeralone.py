from collections import defaultdict, deque

class graph():
    # directed graph
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def insert(self, a, b):
        self.graph[a].extend(b)

    def connection(self, start, finish, explored=None, count=-1):
        if not explored:
            explored = set()
            explored.add(start)
        for i in self.graph[start]:
            count += 1
            if i == finish:
                print('--->'+str(count))
            if i not in explored:
                explored.add(i)
                self.connection(i, finish, explored, count)

    def bfs(self):
        vertices = [i for i in self.graph]
        queue = deque()
        queue.append(vertices[0])
        explored = set()
        explored.add(vertices[0])
        count = -1
        while queue:
            count += 1
            vertex = queue.popleft()
            print(vertex, end=', ')
            for i in self.graph[vertex]:
                if i == finish:
                    print('--->'+str(count))
                if i not in explored:
                    queue.append(i)
                    explored.add(i)
        print('')

g = graph()
for _ in range(int(input())):
    entrada = list(map(int, input().split()))
    key = entrada.pop(0)
    if int(entrada[0]) > 0:
        entrada.pop(0)
        adjs = entrada
        g.insert(key, adjs)

start, finish = map(int, input().split())
response = g.connection(start, finish)
if response is None:
    print('Forevis alonis...')
else: print(response)
