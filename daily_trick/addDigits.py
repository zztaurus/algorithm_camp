
"""

https://leetcode-cn.com/problems/add-digits/

"""


class AddDigits(object):

    def solution(self, num):

        """
        递归解法(找到重复子问题)
        """

        if num < 10:
            return num

        next = 0

        while num != 0:

            next = next + num % 10

            num /= 10

        return self.solution(next)

    def solution_1(self, num):
        """
        :type num: int
        :rtype: int
        """

        while num >= 10:
            num, digit = divmod(num, 10)
            num = num + digit
        return num

    def solution_2(self, num):

        """
        能够被9整除的整数，各位上的数字加起来也必然能被9整除，所以，连续累加起来，最终必然就是9。
        
        不能被9整除的整数，各位上的数字加起来，结果对9取模，和初始数对9取摸，是一样的，所以，连续累加起来，最终必然就是初始数对9取摸。

        xyz = x*100+y*10+z=x*99+y*9+x+y+z

        (x + y + z) % 9 = (xyz) % 9


        if num % 9 == 0:
            return 9
        else:
            return num % 9

        """

        return (num - 1) % 9 + 1


if __name__ == '__main__':

    ad = AddDigits()
    ad.solution_1(388)




