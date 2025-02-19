'''
1249. Minimum Remove to Make Valid Parentheses
Medium
Topics
Companies
Hint
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either '(' , ')', or lowercase English letter.
'''


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        new_s = []
        for i, char in enumerate(s):
            new_s.append(None)
            if char not in ('(', ')'):
                new_s[i] = char
                continue

            if char == '(':
                stack.append((i, char))
            else:
                if stack and stack[-1][1] == '(':
                    new_s[i] = ')'
                    br = stack.pop()
                    new_s[br[0]] = br[1]
                else:
                    continue
        result = ''.join([x for x in new_s if x])
        return result


if __name__ == '__main__':
    s = Solution()

    result = s.minRemoveToMakeValid("lee(t(c)o)de)")
