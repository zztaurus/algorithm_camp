
"""

https://leetcode-cn.com/problems/combinations/

组合

"""

import copy


class Solution(object):

    def combine(self, n, k):

        """
        回溯法：

        【1】 - 【2， 3， 4】
        【2】 - 【3， 4】
        【3】 - 【4】

        """

        res = []
        sub_res = []
        self.back_tracking(n, res, sub_res, 1, k)
        return res

    def back_tracking(self, n, res, sub_res, i, k):

        if len(sub_res) == k:
            res.append(sub_res)
            return

        for num in range(i, n+1):
            sub_res.append(num)
            self.back_tracking(n, res, copy.deepcopy(sub_res), num + 1, k)
            sub_res.remove(num)

    def combine_2(self, n, k):

        """
        基于方法一进行剪枝优化

        """

        res = []
        sub_res = []
        self.back_tracking_2(n, res, sub_res, 1, k)
        return res

    def back_tracking_2(self, n, res, sub_res, i, k):

        if len(sub_res) == k:
            res.append(sub_res)
            return

        for num in range(i, n + 1):
            if n - i + 1 >= k - len(sub_res): # 省的元素无法满足组合中元素个数K的要求
                sub_res.append(num)
                self.back_tracking_2(n, res, copy.deepcopy(sub_res), num + 1, k)
                sub_res.remove(num)


if __name__ == '__main__':

    s = Solution()
    rr = s.combine_2(4, 2)
    print(rr)