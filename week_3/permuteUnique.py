

"""


https://leetcode-cn.com/problems/permutations-ii/

全排列 II


在全排列的基础上如何解决重复问题，

        我们只要设定一个规则，保证在填第 i 个数的时候重复数字只会被填入一次即可。
        而在本题解中，我们选择对原数组排序，保证相同的数字都相邻，
        然后每次填入的数一定是这个数所在重复数集合中「从左往右第一个未被填过的数字


"""

import copy


class Solution(object):

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return []
        nums.sort()  # 有重复元素的问题，通过排序简化
        res = []
        sub_res = []
        n = len(nums)
        visited = [False] * n
        self.back_trace(res, sub_res, nums, visited, n, 0)
        return res

    def back_trace(self, res, sub_res, nums, visited, n, index):

        if index == n:
            res.append(sub_res)
            return

        for i in range(n):
            if visited[i]:
                continue

            if i > 0 and nums[i - 1] == nums[i] and visited[i-1] == False:
                # 每次填入的数一定是这个数所在重复数集合中「从左往右第一个未被填过的数字」。
                continue

            visited[i] = True
            self.back_trace(res, sub_res + nums[i], nums, copy.copy(visited), n, index+1)
            visited[i] = False


if __name__ == '__main__':
    s = Solution()
    s.permuteUnique([1, 1, 2])