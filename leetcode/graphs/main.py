class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, v1, v2, directed=False):
        if v1 not in self.adjacency_list:
            self.add_vertex(v1)
        if v2 not in self.adjacency_list:
            self.add_vertex(v2)

        self.adjacency_list[v1].append(v2)
        if not directed:
            self.adjacency_list[v2].append(v1)

    def get_neighbors(self, vertex):
        return self.adjacency_list.get(vertex, [])

    def __str__(self):
        result = ''
        for vertex, neighbors in self.adjacency_list.items():
            result += f'{vertex}: {neighbors}\n'
        return result


def dfs(graph: Graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start, end=" ")

    for neighbors in graph.get_neighbors(start):
        if neighbors not in visited:
            dfs(graph, neighbors, visited)


def bfs(graph: Graph, start):
    visited = {start}
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")

        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


if __name__ == '__main__':
    g = Graph()

    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    print(g)

    print('DFS:')
    dfs(g, 1)

    print('\n\nBFS:')
    bfs(g, 1)
