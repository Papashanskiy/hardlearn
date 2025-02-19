import unittest

from leetcode.data_strucures.graph.via_adjacency_list import Graph


class TestAdjacencyMatrixGraph(unittest.TestCase):
    def setUp(self):
        # Инициализируем граф, работающий на основе матрицы смежности
        self.graph = Graph()

    def test_add_vertex(self):
        self.graph.add_vertex('A')
        self.assertTrue(self.graph.has_vertex('A'),
                        "Вершина 'A' должна существовать в графе после добавления.")

    def test_add_edge(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_edge('A', 'B')
        # Предполагаем, что граф неориентированный
        self.assertTrue(self.graph.has_edge('A', 'B'),
                        "Ребро (A-B) должно существовать после add_edge.")
        self.assertTrue(self.graph.has_edge('B', 'A'),
                        "Ребро (B-A) должно существовать после add_edge в неориентированном графе.")

    def test_remove_vertex(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_edge('A', 'B')
        self.graph.remove_vertex('A')
        self.assertFalse(self.graph.has_vertex('A'),
                         "Вершина 'A' не должна существовать после remove_vertex.")
        self.assertFalse(self.graph.has_edge('A', 'B'),
                         "После удаления вершины 'A' ребро (A-B) тоже не должно существовать.")

    def test_remove_edge(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_edge('A', 'B')
        self.graph.remove_edge('A', 'B')
        self.assertFalse(self.graph.has_edge('A', 'B'),
                         "Ребро (A-B) не должно существовать после remove_edge.")
        self.assertFalse(self.graph.has_edge('B', 'A'),
                         "Ребро (B-A) не должно существовать после remove_edge в неориентированном графе.")

    def test_has_vertex(self):
        self.graph.add_vertex('A')
        self.assertTrue(self.graph.has_vertex('A'))
        self.assertFalse(self.graph.has_vertex('B'))

    def test_has_edge(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_edge('A', 'B')
        self.assertTrue(self.graph.has_edge('A', 'B'))
        self.assertFalse(self.graph.has_edge('A', 'C'))


if __name__ == '__main__':
    unittest.main()
