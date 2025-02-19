from queue import Queue
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        turns = 0
        visited = set(deadends)
        next_step_map = {'0': '1', '1': '2', '2': '3', '3': '4',
                         '4': '5', '5': '6', '6': '7', '7': '8', '8': '9', '9': '0'}
        prev_step_map = {'0': '9', '9': '8', '8': '7', '7': '6',
                         '6': '5', '5': '4', '4': '3', '3': '2', '2': '1', '1': '0'}
        if '0000' in visited:
            return -1
        queue = Queue()
        queue.put('0000')
        while not queue.empty():
            for _ in range(queue.qsize()):
                cur = queue.get()
                if cur in visited:
                    continue
                visited.add(cur)
                if cur == target:
                    return turns
                for i in range(4):
                    step = list(cur)
                    next_step = step[:]
                    next_step[i] = next_step_map[next_step[i]]
                    next_step = ''.join(next_step)

                    prev_step = step[:]
                    prev_step[i] = prev_step_map[prev_step[i]]
                    prev_step = ''.join(prev_step)

                    if next_step not in visited:
                        queue.put(next_step)
                    if prev_step not in visited:
                        queue.put(prev_step)
            turns += 1
        return -1


def main():
    s = Solution()
    case_1 = (["0201", "0101", "0102", "1212", "2002"], "0202")
    case_2 = (["8888"], "0009")

    result = s.openLock(*case_1)
    assert 6 == result, f'{result=}'
    result = s.openLock(*case_2)
    assert 1 == result, f'{result=}'

    print('OK')


if __name__ == '__main__':
    main()
