from leetcode.data_strucures.graph.via_adjacency_matrix import Graph, matrix_dfs


def test_get_neighbours():
    graph = Graph()

    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')

    assert ['B', 'C'] == graph.get_neighbors('A')
    assert ['A'] == graph.get_neighbors('B')
    assert ['A'] == graph.get_neighbors('C')


def test_dfs():
    graph = Graph()

    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')
    graph.add_vertex('F')
    graph.add_vertex('G')

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'F')
    graph.add_edge('C', 'G')

    assert ['A', 'B', 'D', 'E', 'C', 'F', 'G'] == matrix_dfs(graph, 'A')
