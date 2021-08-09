"""
有效括号

https://leetcode-cn.com/problems/valid-parentheses/

"""


class IsValid(object):

    def solution_1(self, s):
        """
        :type s: str
        :rtype: bool

        利用栈先进后出的特性进行左右括号匹配
        """

        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if stack and i in dic:
                if stack[-1] == dic[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return not stack

