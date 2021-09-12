
"""

https://leetcode-cn.com/problems/house-robber-ii/


打家劫舍 II

"""


class Solution(object):

    def rob(self, nums):
        """

        问题简化

        在不偷窃第一个房子的情况下（即 nums[1:]nums[1:]），最大金额是 p_1

        在不偷窃最后一个房子的情况下（即 nums[:n-1]nums[:n−1]），最大金额是 p_2

        dp[i] 表示前i个房子在满足条件的前提下能盗窃的最大金额

        dp[n+1] = max(dp[n], dp[n-1] + num)

            1. 如果n被偷，那么dp[n+1] = dp[n]
            2. 如果n-1被偷, 那么dp[n+1] = dp[n-1] + nums[n+1]

        记忆化动态规划

        """

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else :
            return max(Solution().rob_2(nums[:-1]), Solution().rob_2(nums[1:]))

    def rob_1(self, nums):
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        dp[2] = max(nums[0], nums[1])
        for i in range(3, len(nums) + 1):
            print(dp, i)
            dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])
        return dp[len(nums)]

    def rob_2(self, nums):

        pre = nums[0]
        cur = max(nums[0], nums[1])
        for i in range(3, len(nums) + 1):
            cur, pre = max(pre + nums[i-1], cur), cur
        return cur

    def rob_3(self, nums):

        """

        基于方法一进行优化, 因为只需要记忆dp[i-1], dp[i-2], 所以去掉dp数组, 优化空间复杂度。

        """

        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur

        return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    res = max(Solution().rob(nums[:-1]), Solution().rob(nums[1:]))
    print(res)
