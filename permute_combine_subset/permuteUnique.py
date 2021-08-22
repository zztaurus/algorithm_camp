

"""


https://leetcode-cn.com/problems/permutations-ii/

全排列 II


在全排列的基础上如何解决重复问题，

        我们只要设定一个规则，保证在填第 i 个数的时候重复数字只会被填入一次即可。
        而在本题解中，我们选择对原数组排序，保证相同的数字都相邻，
        然后每次填入的数一定是这个数所在重复数集合中「从左往右第一个未被填过的数字


        加上 !vis[i - 1]来去重主要是通过限制一下两个相邻的重复数字的访问顺序

       举个栗子，对于两个相同的数11，我们将其命名为1a1b, 1a表示第一个1，1b表示第二个1； 那么，不做去重的话，会有两种重复排列 1a1b, 1b1a， 我们只需要取其中任意一种排列； 为了达到这个目的，限制一下1a, 1b访问顺序即可。 比如我们只取1a1b那个排列的话，只有当visit nums[i-1]之后我们才去visit nums[i]， 也就是如果!visited[i-1]的话则continue


"""

import copy


class Solution(object):

    def permuteUnique(self, nums):
        """

        时间复杂度：O(n×n!)，其中 n 为序列的长度。

        空间复杂度: 我们需要 O(n) 的标记数组，同时在递归的时候栈深度会达到 O(n)，因此总空间复杂度为 O(n + n)=O(2n)=O(n)。

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


                """
                
                加上 !vis[i - 1]
                来去重主要是通过限制一下两个相邻的重复数字的访问顺序

                举个栗子，对于两个相同的数11，我们将其命名为1a1b, 1
                a表示第一个1，1b表示第二个1； 那么，不做去重的话，会有两种重复排列1a1b, 1b1a， 我们只需要取其中任意一种排列； 
                为了达到这个目的，限制一下1a, 1b访问顺序即可。 比如我们只取1a1b那个排列的话，只有当 visit nums[i - 1]
                之后我们才去visit nums[i]， 也就是如果!visited[i - 1]的话则continue
        
                """

                continue

            visited[i] = True
            self.back_trace(res, sub_res + nums[i], nums, copy.copy(visited), n, index+1)
            visited[i] = False


if __name__ == '__main__':
    s = Solution()
    s.permuteUnique([1, 1, 2])