
'''
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

核心思路: 由末位向首位行进，如果需要进位，那么下一位加一, 如果所有位都加一，那就是出现了都是9的情况，那么在数组首位插入 1

'''


class Solution(object):

    def plus_one(self, digits):
        """
        :type n: int
        :rtype: int
        """

        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits

    def plus_one2(self, digits):
        """
        :type n: int
        :rtype: int
        """

        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            digits[i] %= 10
            if digits[i] != 0:
                return digits
        digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    s = Solution()
    res = s.plus_one([8, 9, 9, 9])
    print(res)
