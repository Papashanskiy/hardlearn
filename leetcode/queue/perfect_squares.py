"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, 
it is the product of some integer with itself. For example, 1, 4, 9, and 16 are 
perfect squares while 3 and 11 are not.


Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 

Constraints:

1 <= n <= 10^4
"""

import math
from queue import Queue


class Solution:
    def numSquares(self, n: int) -> int:
        max_number = round(math.sqrt(n))
        all_perfect_squares = tuple(x*x for x in range(1, max_number))

        steps = 0
        queue = Queue()
        queue.put(0)

        while not queue.empty():
            for _ in range(queue.qsize()):
                element = queue.get()
                if element == n:
                    break
                for square in all_perfect_squares:
                    queue.put(element + square)
            steps += 1

        return steps


if __name__ == '__main__':
    s = Solution()

    # case_1 = 12
    # result = s.numSquares(case_1)
    # assert result == 3, f'{result=}'
    # s = Solution()

    # case_2 = 13
    # result = s.numSquares(case_2)
    # assert result == 2, f'{result=}'

    case_3 = 4
    result = s.numSquares(case_3)
    assert result == 1, f'{result=}'

    print('OK')
