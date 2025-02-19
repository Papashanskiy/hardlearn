'''
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have 
to wait after the ith day to get a warmer temperature. If there is no future 
day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]

        solution = [0] * len(temperatures)
        stack = [(0, temperatures[0])]
        for i in range(1, len(temperatures)):
            if temperatures[i] <= stack[-1][1]:
                stack.append((i, temperatures[i]))
            else:
                while stack:
                    latest = stack[-1]
                    if latest[1] < temperatures[i]:
                        solution[latest[0]] = i - latest[0]
                        stack.pop()
                    else:
                        break
                stack.append((i, temperatures[i]))
        return solution


if __name__ == '__main__':
    s = Solution()

    case = [73, 74, 75, 71, 69, 72, 76, 73]
    solution = s.dailyTemperatures(case)
    output = [1, 1, 4, 2, 1, 1, 0, 0]
    assert solution == output, f'{solution=}'

    case = [30, 40, 50, 60]
    solution = s.dailyTemperatures(case)
    output = [1, 1, 1, 0]
    assert solution == output, f'{solution=}'

    case = [30, 60, 90]
    solution = s.dailyTemperatures(case)
    output = [1, 1, 0]
    assert solution == output, f'{solution=}'

    case = [75, 71, 69, 70, 73, 73]
    solution = s.dailyTemperatures(case)
    output = [0, 3, 1, 1, 0, 0]
    assert solution == output, f'{solution=}'

    print('OK')
