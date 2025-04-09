class Graph:
    def __init__(self):
        self.vertex_map = {}
        self.invert_vertex_map = {}
        self.adjacency_matrix = []

    def add_vertex(self, vertex):
        if vertex not in self.vertex_map:
            self.vertex_map[vertex] = len(self.adjacency_matrix)
            self.invert_vertex_map[len(self.adjacency_matrix)] = vertex
            for row in self.adjacency_matrix:
                row.append(0)
            self.adjacency_matrix.append(
                [0] * (len(self.adjacency_matrix) + 1))

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertex_map and vertex2 in self.vertex_map:
            v1_index = self.vertex_map[vertex1]
            v2_index = self.vertex_map[vertex2]
            self.adjacency_matrix[v1_index][v2_index] = 1
            self.adjacency_matrix[v2_index][v1_index] = 1

    def remove_vertex(self, vertex):
        if vertex in self.vertex_map:
            v_index = self.vertex_map[vertex]
            del self.vertex_map[vertex]
            self.adjacency_matrxi.pop(v_index)
            for row in self.adjacency_matrix:
                row.remove(v_index)

            for v, idx in self.vertex_map.items():
                if idx > v_index:
                    self.vertex_map[v] = idx - 1

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.vertex_map and vertex2 in self.vertex_map:
            v1_index = self.vertex_map[vertex1]
            v2_index = self.vertex_map[vertex2]
            self.adjacency_matrix[v1_index][v2_index] = 0
            self.adjacency_matrix[v2_index][v1_index] = 0

    def has_vertex(self, vertex):
        if vertex in self.vertex_map:
            return True
        return False

    def get_neighbors(self, vertex):
        if vertex not in self.vertex_map:
            return []

        vertex_idx_in_matrix = self.vertex_map[vertex]

        neighbors = []
        for i in range(len(self.adjacency_matrix[vertex_idx_in_matrix])):
            if self.adjacency_matrix[vertex_idx_in_matrix][i]:
                neighbors.append(self.invert_vertex_map[i])

        return neighbors

    def has_edge(self, vertex1, vertex2):
        if vertex1 in self.vertex_map and vertex2 in self.vertex_map:
            if self.adjacency_matrix[self.vertex_map[vertex1]][self.vertex_map[vertex2]] == 1:
                return True
        return False

    def __str__(self):
        """
        Возвращаем удобочитаемое представление:
        - Отображение вершин и их индексов
        - Содержимое матрицы смежности
        """
        output = ["Vertex map: " + str(self.vertex_map)]
        output.append("Adjacency matrix:")
        for row in self.adjacency_matrix:
            output.append(str(row))
        return "\n".join(output)


def matrix_dfs(graph: Graph, start, visited=None, result=None):
    if not graph.has_vertex(start):
        raise ValueError(f'Graph {graph} does not include value {start}')

    if not visited:
        visited = set()

    if not result:
        result = []

    if start in visited:
        return

    result.append(start)
    visited.add(start)

    for neighbor in graph.get_neighbors(start):
        matrix_dfs(graph, neighbor, visited, result)

    return result
