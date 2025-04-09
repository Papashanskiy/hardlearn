from math import inf
from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        min_length = inf
        last_seen = {}

        for i in range(len(cards)):
            if cards[i] in last_seen:
                min_length = min(min_length, i - last_seen[cards[i]] + 1)
            last_seen[cards[i]] = i

        if min_length == inf:
            return -1

        return min_length
