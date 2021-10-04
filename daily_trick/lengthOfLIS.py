
"""

https://leetcode-cn.com/problems/longest-increasing-subsequence/


最长递增子序列


"""


class Solution(object):

    def lengthOfLIS(self, nums):
        """
        动态规划

        状态定义：

        dp[i]dp[i] 的值代表 nums 以 nums[i]nums[i] 结尾的最长子序列长度。
        转移方程： 设 j∈[0,i)j∈[0,i)，考虑每轮计算新 dp[i]dp[i] 时，遍历 [0,i)[0,i) 列表区间，做以下判断：

        当 nums[i] > nums[j]nums[i]>nums[j] 时： nums[i]nums[i] 可以接在 nums[j]nums[j] 之后（此题要求严格递增），此情况下最长上升子序列长度为 dp[j] + 1dp[j]+1 ；
        当 nums[i] <= nums[j]nums[i]<=nums[j] 时： nums[i]nums[i] 无法接在 nums[j]nums[j] 之后，此情况上升子序列不成立，跳过。
        上述所有 1. 情况 下计算出的 dp[j] + 1dp[j]+1 的最大值，为直到 ii 的最长上升子序列长度（即 dp[i]dp[i] ）。实现方式为遍历 jj 时，每轮执行 dp[i] = max(dp[i], dp[j] + 1)dp[i]=max(dp[i],dp[j]+1)。
        转移方程： dp[i] = max(dp[i], dp[j] + 1) for j in [0, i)。
        初始状态：

        dp[i] 所有元素置 1，含义是每个元素都至少可以单独成为子序列，此时长度都为 1。
        返回值：

        返回 dp 列表最大值，即可得到全局最长上升子序列长度。

        """

        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)