
# Definition for a Node.
from collections import deque
from typing import List, Optional


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        levels = []
        nodes = deque()
        nodes.appendleft((root, 0))

        while nodes:
            node, level = nodes.pop()
            if node:
                if level >= len(levels):
                    levels.append([])
                levels[level].append(node.val)
                if node.children:
                    for child in node.children:
                        nodes.appendleft((child, level+1))
        return levels


if __name__ == '__main__':
    s = Solution()

    case_1 = Node(
        val=1,
        children=[
            Node(
                val=3,
                children=[
                    Node(val=5),
                    Node(val=6)
                ]
            ),
            Node(val=2),
            Node(val=4)
        ]
    )
    result = s.levelOrder(case_1)
    assert [[1], [3, 2, 4], [5, 6]] == result, f'{result=}'

    case_2 = None
    result = s.levelOrder(case_2)
    assert [] == result, f'{result=}'

    print('OK')
