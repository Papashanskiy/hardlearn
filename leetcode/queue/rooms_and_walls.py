from queue import Queue
from typing import List


class Point:
    def __init__(self, row, col):
        self.row: int = row
        self.col: int = col


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        GATE = 0
        WALL = -1
        EMPTY_ROOM = 2147483647
        
        DIRECTIONS = (
            Point(1, 0),
            Point(0, 1),
            Point(-1, 0),
            Point(0, -1)
        )
        
        x = len(rooms)
        if x == 0:
            return
        y = len(rooms[0])
        queue = Queue()
        
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == GATE:
                    queue.put(Point(i, j))
        
        while not queue.empty():
            point = queue.get()
            
            for direction in DIRECTIONS:
                next_point = Point(point.row + direction.row, point.col + direction.col)
                if (
                    next_point.row < 0 or next_point.col < 0 
                    or next_point.row >= x or next_point.col >= y 
                    or rooms[next_point.row][next_point.col] != EMPTY_ROOM
                ):
                    continue
                rooms[next_point.row][next_point.col] = rooms[point.row][point.col] + 1               
                queue.put(next_point)


def main():
    solution = Solution()
    
    rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    solution.wallsAndGates(rooms)
    print(rooms)
    assert rooms == [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]


if __name__ == '__main__':
    main()
