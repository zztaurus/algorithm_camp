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

        p, q, r = 0, 0, 1
        for i in range(1, n+1):
            p = q
            q = r
            r = p + q
        return r
