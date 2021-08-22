
"""

https://leetcode-cn.com/problems/subsets/

子集

"""

import copy


class Solution(object):

    def subsets(self, nums):


        """

        [[]]

        [[], [1]]

        [[], [1], [2], [1, 2]]

        [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

        时间复杂度：

        空间复杂度：

        """

        res = [[]]   # 初始化时，结果集中包含一个空子集

        for num in nums:

            res = res + [sub_set + [num] for sub_set in res]
        return res

    def subsets_2(self, nums):

        """
        python 中对于list对象，

        时间复杂度：O(n * n)

        空间复杂度：O(n)

        """

        if not nums:
            return

        res = []
        sub_set = []

        def dfs(res, sub_set, nums, index):

            if index == len(nums):
                res.append(sub_set)
                return  # 终止递归

            i = index + 1
            dfs(res, copy.copy(sub_set), nums, i)  # 不选择当前元素
            sub_set.append(nums[index])
            dfs(res, copy.copy(sub_set), nums, i)  # 选择当前元素

        dfs(res, sub_set, nums, 0)
        return res


if __name__ == '__main__':

    s = Solution()
    s.subsets([1, 2, 3])
