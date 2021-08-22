import copy

"""

https://leetcode-cn.com/problems/generate-parentheses/ 


括号生成

"""

class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        left = right = 0
        s = []
        res = []
        return self.generate(left, right, n, s, res)

    def generate(self, left, right, n, s, res):

        """
        思路:

        只在序列仍然保持有效时才添加 '(' or ')'，而不是每次随意添加左右括号。

        通过跟踪到目前为止放置的左括号和右括号的数目来做到这一点，

        如果左括号数量不大于 n，我们可以放一个左括号。如果右括号数量小于左括号的数量，我们可以放一个右括号。

        """

        if len(s) == 2 * n:
            res.append(''.join(s))
            return res

        if left < n:
            s.append('(')
            self.generate(left + 1, right, n, copy.deepcopy(s), res)
            s.pop()

        if right < left:
            s.append(')')
            self.generate(left, right + 1, n, copy.deepcopy(s), res)
            s.pop()

        return res

    def valid(self, s):

        """

        验证括号是否有效

        """
        bal = 0
        for c in s:
            if c == '(':
                bal += 1
            else:
                bal -= 1
            if bal < 0: return False
        return bal == 0


if __name__ == '__main__':

    s = Solution()
    res = s.generateParenthesis(3)
    print(res)