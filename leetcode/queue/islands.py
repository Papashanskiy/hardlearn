from queue import Queue
from typing import List


class Point:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col


DIRECTIONS = (
    Point(1, 0),
    Point(0, 1),
    Point(-1, 0),
    Point(0, -1),
)


EMPTY = '0'
FILLED = '1'


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        queue = Queue()
        rows = len(grid)
        cols = len(grid[0])

        num_of_islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == FILLED:
                    num_of_islands += 1
                    queue.put(Point(i, j))
                    grid[i][j] = EMPTY
                    while not queue.empty():
                        point = queue.get()
                        for direction in DIRECTIONS:
                            new_point = Point(
                                point.row + direction.row, point.col + direction.col
                            )
                            if (
                                new_point.row < 0
                                or new_point.col < 0
                                or new_point.row > rows - 1
                                or new_point.col > cols - 1
                            ):
                                continue
                            if grid[new_point.row][new_point.col] == FILLED:
                                grid[new_point.row][new_point.col] = EMPTY
                                queue.put(new_point)
        return num_of_islands


def main():
    case_1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    case_2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    s = Solution()

    assert 1 == s.numIslands(case_1)
    assert 3 == s.numIslands(case_2)

    print('OK')


if __name__ == '__main__':
    main()
