class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        执行用时：12 ms
        """
        j = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                if i != j:
                    nums[i] = 0

                j += 1


    def moveZeros1(self, nums):

        """

        :param nums:
        :return:
        如果数组中不存在0，那么 i，j 应该是保存同步的，如果存在0，那么j应该会落后于i
        """

        j = 0

        for i in range(0, len(nums)):

            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1

        print(nums)


    def moveZeroes2(self, nums):

        last_noze_zero_found_at = 0

        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[last_noze_zero_found_at] = nums[i]
                last_noze_zero_found_at += 1

        for i in range(last_noze_zero_found_at, len(nums)):
            nums[i] = 0

        print(nums)

    def moveZeroes3(self, nums):

        '''

        :param nums:
        :return:

        执行用时：140 ms
        '''

        for i in range(0, len(nums)):
            if nums[i] == 0:
                nums.append(0)
                nums.remove(0)


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    s.moveZeros1(nums)

