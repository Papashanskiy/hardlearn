class MatrixGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, v1, v2, directed=False):

        self.adjacency_matrix[v1][v2] = 1
        if not directed:
            self.adjacency_matrix[v2][v1] = 1

    def has_edge(self, v1, v2):
        return self.adjacency_matrix[v1][v2] != 0

    def __str__(self):
        result = ""

        for row in self.adjacency_matrix:
            result += f'{row}\n'

        return result


if __name__ == "__main__":
    mg = MatrixGraph(4)
    mg.add_edge(0, 1)
    mg.add_edge(0, 3)
    mg.add_edge(1, 2)
    mg.add_edge(2, 3)

    print(mg)
