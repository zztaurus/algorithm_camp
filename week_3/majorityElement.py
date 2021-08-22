
"""

https://leetcode-cn.com/problems/majority-element/

多数元素


思路一: 哈希表法


思路二：排序法


思路三: 分治法


思路四: 摩尔投票法


"""

import random

class Solution(object):


    def majorityElement_2(self, nums):

        """

        随机化

        最坏时间复杂度 O(正无穷)

        """

        majority_count = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate


    def majorityElement_3(self, nums):

        """

        分治法:

        如果数 a 是数组 nums 的众数，如果我们将 nums 分成两部分，那么 a 必定是至少一部分的众数。

        我们可以使用反证法来证明这个结论。假设 a 既不是左半部分的众数，也不是右半部分的众数，

        那么 a 出现的次数少于 l / 2 + r / 2 次，其中 l 和 r 分别是左半部分和右半部分的长度。由于 l / 2 + r / 2 <= (l + r) / 2，

        说明 a 也不是数组 nums 的众数，因此出现了矛盾。所以这个结论是正确的。

        使用经典的分治算法递归求解，直到所有的子问题都是长度为 1 的数组。长度为 1 的子数组中唯一的数显然是众数，直接返回即可。

        如果回溯后某区间的长度大于 1，我们必须将左右子区间的值合并。如果它们的众数相同，那么显然这一段区间的众数是它们相同的值。

        否则，我们需要比较两个众数在整个区间内出现的次数来决定该区间的众数。


        """

        def majority_element_rec(lo, hi) -> int:

            # 递归终止

            if lo == hi:  # 剩余一个元素
                return nums[lo]

            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)  # 左半部分
            right = majority_element_rec(mid+1, hi)  # 右半部分

            if left == right:
                return left

            left_count = sum(1 for i in range(1, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(1, hi+1) if nums[i] == right)

            return left if left_count > right_count else right  # 如果数 a 是数组 nums 的众数，如果我们将 nums 分成两部分，那么 a 必定是至少一部分的众数。

        return majority_element_rec(1, len(nums) - 1)

    def majorityElement_4(self, nums):

        """

        Boyer-Moore 投票算法

        如果我们把众数记为 +1+1，把其他数记为 -1−1，将它们全部加起来，显然和大于 0，从结果本身我们可以看出众数比其他数多。

        时间复杂度 O(n)

        空间复杂度 O(1)

        """

        more_num = nums[0]
        count = 0
        for num in nums:
            if count == 0:
                more_num = num

            count += 1 if num == more_num else -1

        return more_num


if __name__ == '__main__':

    s = Solution()
    s.majorityElement_4([6, 5, 5])


