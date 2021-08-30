
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
        for v in g:
            n = self.binarySearchOne(v, s)
            print(v, n)
            if n and len(s):
                count += 1
            else:
                break
        return count

    def binarySearchOne(self, target, num): # TODO modify 

        left = 0
        right = len(num) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if num[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return left


if __name__ == '__main__':

    g = [1, 2, 3]
    s = [1, 2, 2]
    count = Solution().findContentChildren_2(g, s)










