'''

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。


输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1].

'''


class TwoSum(object):

    def solution_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        两遍哈希法： 利用Hash表查找O(1)的特性简化了问题。
        """

        hm = dict()
        for index, value in enumerate(nums):
            hm.update({value: index})

        for index, value in enumerate(nums):
            j = hm.get(target-value)
            if j is not None and j != index:
                return [index, j]

    def solution_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        一遍哈希法： 从 a 查找到 target-a, 也可以从 target-a 查找到 a, 所以优化两边哈希法为一遍哈希法。
        """

        hm = dict()
        for index, value in enumerate(nums):
            a_t = target - value
            if a_t in hm:
                return [index, hm.get(a_t)]
            else:
                hm.update({value: index})




if __name__ == '__main__':
    nums = [1, 3, 4, 2]
    s = TwoSum()
    res = s.solution_1(nums, 6)
    print(res)


