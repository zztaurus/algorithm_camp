
"""

https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/

电话号码的字母组合


思路一: DFS


思路二: BFS

"""

import copy


class Solution(object):

    def letterCombinations(self, digits):

        """

        时间复杂度: O(3^m * 4^n)

        空间复杂度: O(3^m * 4^n)

        """

        if not digits:
            return []

        res = []
        ans = ''
        char_map = {
                 '2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def back_tracking(res, ans, char_map, digits, index):

            # 递归终止

            if index == len(digits):
                res.append(ans)
                return

            # process
            for char in char_map[digits[index]]:
                back_tracking(res, ans + char, char_map, digits, index+1)
        back_tracking(res, ans, char_map, digits, 0)
        return res

    def letterCombinations_2(self, digits):

        """

        方法一代码简化
        """

        if not digits:
            return []

        res = []
        ans = ''
        char_map = {
                 '2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def back_tracking(ans, next_digit):

            # 递归终止

            if len(next_digit) == 0:
                res.append(ans)
                return

            # process
            for char in char_map[next_digit[0]]:
                back_tracking(ans + char, next_digit[1: ])
        back_tracking(ans, digits)
        return res

    def letterCombinations_3(self, digits):

        """

        队列

        """

        if not digits: return []
        char_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']}

        queue = ['']  # 初始化队列
        for digit in digits:
            n = len(queue)  # 程序遍历，每一层的宽度。
            for _ in range(n):
                tmp = queue.pop(0)
                for char in char_map[digit]:
                    queue.append(tmp + char)

        return queue


if __name__ == '__main__':

    s = Solution()
    s.letterCombinations("999")