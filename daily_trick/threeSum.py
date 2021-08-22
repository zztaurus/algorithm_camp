
"""

https://leetcode-cn.com/problems/3sum/

三数之和

"""


class ThreeSum(object):


    def solution_2(self, nums):

        """

        :param nums:
        :return:

        排序 + 双指针

        时间复杂度: O(n * n)

        空间复杂度：O(1)


        """

        n = len(nums)
        res = []
        if not nums or n < 3:
            print(nums)
            return []

        nums.sort()

        for i in range(n):

            if nums[i] > 0:  # 如果i大于0，那么三数之和一定大约0
                return res

            if i > 0 and nums[i] == nums[i - 1]: # 去重
                continue

            l = i + 1
            r = n - 1

            while l < r:
                
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:  # 去重
                        l += + 1
                    while l < r and nums[r] == nums[r - 1]:  # 去重
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] > 0: # 大于0，r太大
                    r -= 1
                else:
                    l += 1   # 小于0，l太小

        return res


if __name__ == '__main__':

    nums = [0, 0, 0]
    ThreeSum().solution_2(nums)