'''
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
'''

from typing import List


def sum_(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return int(a / b)


operations = {
    '+': sum_,
    '-': sub,
    '*': mul,
    '/': div
}


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) == 1:
            return int(tokens[0])

        stack = []

        for t in tokens:
            if t in operations.keys():
                n1, n2 = int(stack.pop()), int(stack.pop())
                stack.append(operations.get(t)(n2, n1))
                continue
            stack.append(t)

        return stack.pop()


if __name__ == '__main__':
    s = Solution()

    arg = ["2", "1", "+", "3", "*"]
    solution = s.evalRPN(arg)
    expected = 9
    assert expected == solution, f'{expected=} != {solution=}'

    arg = ["4", "13", "5", "/", "+"]
    solution = s.evalRPN(arg)
    expected = 6
    assert expected == solution, f'{expected=} != {solution=}'

    arg = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    solution = s.evalRPN(arg)
    expected = 22
    assert expected == solution, f'{expected=} != {solution=}'

    print('OK')
