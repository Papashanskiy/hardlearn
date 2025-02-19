class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            for vert in self.adjacency_list[vertex]:
                self.adjacency_list[vert].remove(vertex)

            del self.adjacency_list[vertex]

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].remove(vertex2)
            self.adjacency_list[vertex2].remove(vertex1)

    def has_vertex(self, vertex):
        if vertex in self.adjacency_list:
            return True
        return False

    def has_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            if vertex1 in self.adjacency_list[vertex2] and vertex2 in self.adjacency_list[vertex1]:
                return True
        return False

    def __str__(self):
        return str(self.adjacency_list)
