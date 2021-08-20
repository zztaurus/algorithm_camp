# -*- coding: utf-8 -*-


"""

https://ltcode-cn.com/problems/climbing-stairs/

爬楼梯




"""


class Solution(object):
    dp = {1: 1, 2: 2}

    def climbStairs(self, n):
        """

        时间复杂度: O(n)

        空间复杂度: O(1)


        """

        pre_of_pre, pre, cur = 1, 2, 1

        for i in range(3, n):
            cur = pre + pre_of_pre
            pre_of_pre = pre
            pre = cur

        return cur
