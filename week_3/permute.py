
"""

https://tcode-cn.com/problems/permutations/


全排列


"""

import copy


class Solution(object):

    def permute(self, nums):

        """
        时间复杂度：O(n×n!)，其中 n 为序列的长度。

        空间复杂度：O(n)，其中 nn 为序列的长度。除答案数组以外，递归函数在递归过程中需要为每一层递归函数分配栈空间，所以这里需要额外的空间且该空间取决于递归的深度，这里可知递归调用深度为 O(n)O(n)。


        """

        res = []
        sub_res = []
        visited = {}
        for index, val in enumerate(nums):
            visited.update({index:False})

        self.back_tracking(nums, res, sub_res, visited)
        return res

    def back_tracking(self, nums, res, sub_res, visited):

        if len(sub_res) == len(nums):
            res.append(sub_res)
            return

        for index, val in enumerate(nums):
            if not visited[index]:
                sub_res.append(val)
                visited[index] = True
                self.back_tracking(nums, res, copy.deepcopy(sub_res), visited)
                sub_res.remove(val)
                visited[index] = False

    def permute_2(self, nums):


        """

        本质上还是回溯法，但是通过维护一个动态维护nums以取消visiteds数组。

        """

        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        print(res)
        return res


if __name__ == '__main__':

    s = Solution()
    s.permute([1, 2, 3])
    s.permute_2([1, 2, 3])
