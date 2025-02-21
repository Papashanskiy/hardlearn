from collections import Counter
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.m, self.n = len(board), len(board[0])

        board_counter = Counter(char for row in board for char in row)
        word_counter = Counter(word)

        for char in word_counter:
            if word_counter[char] > board_counter.get(char, 0):
                return False

        if word_counter[word[0]] > word_counter[word[-1]]:
            word = word[::-1]

        for i in range(self.m):
            for j in range(self.n):
                if self.dfs(i, j, word):
                    return True

        return False

    def dfs(self, m, n, target):
        if len(target) == 0:
            return True

        if (
            m < 0 or m >= self.m
            or n < 0 or n >= self.n
            or self.board[m][n] != target[0]
        ):
            return False

        self.board[m][n] = '#'

        result = False
        for i_offset, j_offset in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            result = self.dfs(m + i_offset, n + j_offset, target[1:])

            if result:
                break

        self.board[m][n] = target[0]

        return result
