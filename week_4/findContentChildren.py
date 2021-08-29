
"""
https://leetcode-cn.com/problems/assign-cookies/

分发饼干
"""


class Solution(object):

    def findContentChildren(self, g, s):

        """

        贪心算法, 尽可能使用较小的饼干满足每一个孩子，使用饼干的利用率最大化

        """

        g.sort()
        s.sort()
        len_g = len(g)
        len_s = len(s)
        i = j = count = 0
        while i < len_g and j < len_s:
            while j < len_s and g[i] > s[j]:
                j += 1

            if j < len_s:  # 找到一块合适的饼干
                count += 1

            i += 1
            j += 1

            return count

    def findContentChildren_2(self, g, s):

        """

        贪心加二分

        贪心：尽可能使用较小的饼干满足每一个孩子，使用饼干的利用率最大化,

        二分：找到第一一个尺寸大于等于孩子胃口的饼干

        """

        g.sort()
        s.sort()
        count = 0
        for i in range(g):


    def ()






