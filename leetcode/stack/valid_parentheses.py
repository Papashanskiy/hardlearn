'''
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true
'''


class Solution:
    def isValid(self, s: str) -> bool:
        BMAP = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
                continue

            if stack[-1] == BMAP.get(char):
                stack.pop()
                continue

            stack.append(char)

        if stack:
            return False
        return True


if __name__ == '__main__':
    s = Solution()

    case = "()"
    result = s.isValid(case)
    assert result is True, f'{result}'

    case = "()[]{}"
    result = s.isValid(case)
    assert result is True, f'{result}'

    case = "(]"
    result = s.isValid(case)
    assert result is False, f'{result}'

    case = "([])"
    result = s.isValid(case)
    assert result is True, f'{result}'

    case = "([{}(]])"
    result = s.isValid(case)
    assert result is False, f'{result}'

    case = "({[)"
    result = s.isValid(case)
    assert result is False, f'{result}'

    print('OK')
