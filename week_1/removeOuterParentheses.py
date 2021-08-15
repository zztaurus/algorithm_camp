"""

https://leetcode-cn.com/problems/remove-outermost-parentheses/

"""

class RemoveOuterParentheses(object):

    def solution_1(self, s):
        """
        :type s: str
        :rtype: str

        使用下标栈分割原始字符串
        """
        ret = ""
        stack = []
        for index, ch in enumerate(s):
            if ch == '(':
                stack.append(index)
            else:
                left = stack.pop()
                if not stack:
                    ret += s[left + 1:index]  # left:i+1 是分割后的子字符串， left+1:i 为去掉最外层括号后的字符串
        return ret

    def solution_2(self, s):
        """
        :type s: str
        :rtype: str
        计数法
        """

        level = 0
        ans = ''

        for ch in s:
            if ch == '(':
                level += 1
            if level > 1:
                ans += ch
            if ch == ')':
                level -= 1

        return ans


if __name__ == '__main__':
    ro = RemoveOuterParentheses()
    "(())"
    res = ro.solution_2("(()())(())(()(()))")
    print(res)
