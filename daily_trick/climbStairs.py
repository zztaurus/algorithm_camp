"""

https://leetcode-cn.com/problems/climbing-stairs/

爬楼梯



"""

class Solution(object):
    dp = {1: 1, 2: 2}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        pre_of_pre, pre, cur = 1, 2, 1

        for i in range(3, n):
            cur = pre + pre_of_pre
            pre_of_pre = pre
            pre = cur

        return cur
