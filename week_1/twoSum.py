'''

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。


输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1].

'''


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hm = dict()
        for index, value in enumerate(nums):
            print(index)
            hm.update({value: index})

        for index, value in enumerate(nums):
            print(index, value)
            j = hm.get(target-value)
            if j is not None and j != index:
                return [index, j]


if __name__ == '__main__':
    nums = [1, 3, 4, 2]
    s = Solution()
    res = s.twoSum(nums, 6)
    print(res)


