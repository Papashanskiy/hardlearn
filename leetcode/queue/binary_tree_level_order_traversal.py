from collections import deque
from queue import Queue
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = []
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            level = []
            queue_size = queue.qsize()
            for _ in range(queue_size):
                node = queue.get()
                level.append(node.val)
                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)
            levels.append(level)
        return levels


class Solution2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        solution = []
        nodes = deque()
        nodes.appendleft((root, 0))

        while nodes:
            node, level = nodes.pop()
            if node:
                if level >= len(solution):
                    solution.append([])
                solution[level].append(node.val)
                nodes.appendleft((node.left, level+1))
                nodes.appendleft((node.right, level+1))
        return solution


def main():
    s = Solution2()

    case_1 = TreeNode(
        val=3,
        left=TreeNode(
            val=9
        ),
        right=TreeNode(
            val=20,
            left=TreeNode(
                val=15
            ),
            right=TreeNode(
                val=7
            )
        )
    )
    result = s.levelOrder(case_1)
    assert [[3], [9, 20], [15, 7]] == result, f'{result=}'

    case_1 = TreeNode(val=1)
    result = s.levelOrder(case_1)
    assert [[1]] == result, f'{result=}'

    case_1 = None
    result = s.levelOrder(case_1)
    assert [] == result, f'{result=}'

    print('OK')


if __name__ == '__main__':
    main()
