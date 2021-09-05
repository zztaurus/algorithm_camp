
"""

https://leetcode-cn.com/problems/4sum/

四数之和

"""


class Solution(object):

    def fourSum(self, nums, target):

        """
        排序 + 双指针

        时间复杂度: O(n^3)  三层循环

        空间复杂度: O(logn) 排序时间复杂度

        """

        quadruplets = list()
        if not nums or len(nums) < 4:  # 边界条件
            return quadruplets

        nums.sort()  # 升序排序, 双指针法的前提
        length = len(nums)
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:  # 解决重复数字的问题
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:  # 以 nums[i] 为第一个元素，无法找到四元组
                break
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target: # 以 nums[i] 为第一个元素，倒数三个元素为其他三个元素之和小于target，则nums[i] 过小, 继续向后遍历
                continue
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  # 解决重复数字的问题
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:  # 剪枝
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:  # 剪枝
                    continue
                left, right = j + 1, length - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]  # 选定i和j, 问题转换双指针法求为两数之和
                    if total == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:  # 解决重复数字的问题
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right - 1]:  # 解决重复数字的问题
                            right -= 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return quadruplets
