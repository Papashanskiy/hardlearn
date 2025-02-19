'''
227. Basic Calculator II
Attempted
Medium
Topics
Companies
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
'''
from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        def sum_(a, b): return a + b
        def dif(a, b): return a - b
        def mul(a, b): return a * b
        def div(a, b): return int(a / b)

        ops = {
            '+': sum_,
            '-': dif,
            '*': mul,
            '/': div
        }

        stack = []
        last_op = None

        for char in s:
            if char == ' ':
                continue

            if char not in ops:
                if stack and stack[-1] not in ops:
                    value = stack.pop() * 10 + int(char)
                    stack.append(value)
                else:
                    stack.append(int(char))
            else:
                if last_op and last_op in ('*', '/'):
                    n2 = stack.pop()
                    op = stack.pop()
                    n1 = stack.pop()
                    value = ops[op](n1, n2)
                    stack.append(value)
                    last_op = char
                    stack.append(char)
                else:
                    last_op = char
                    stack.append(char)

        if len(stack) != 1 and last_op and last_op in ('*', '/'):
            n2 = stack.pop()
            op = stack.pop()
            n1 = stack.pop()
            value = ops[op](n1, n2)
            stack.append(value)

        if len(stack) == 1:
            return stack.pop()

        q = deque(stack)
        while len(q) != 1:
            n1 = q.popleft()
            op = q.popleft()
            n2 = q.popleft()
            value = ops[op](n1, n2)
            q.appendleft(value)

        return q.pop()
