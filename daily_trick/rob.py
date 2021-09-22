
"""


https://leetcode-cn.com/problems/house-robber/


198. 打家劫舍


"""


class Solution(object):

    def rob(self, nums):

        """

        状态定义:
            dp[i] 表示前i间房子能够偷窃的最高金额

        dp[i+1] = max(nums[i] + dp[i-2], dp[i-1])


        初始状态:

            dp[0] = 0


        返回值:

            返回 dp 列表最后一个元素值，即所有房间的最大偷窃价值。


        """

        N = len(nums)
        dp = [0] * (N + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for k in range(2, N + 1):
            dp[k] = max(dp[k - 1], nums[k - 1] + dp[k - 2])
        return dp[N]

    def rob2(self, nums):

        """

        简化时间复杂度:


             我们发现 dp[n] 只与 dp[n-1] 和 dp[n-2]有关系，因此我们可以设两个变量 cur和 pre 交替记录，将空间复杂度降到 O(1) 。

        """

        pre, cur = 0, 0
        for num in nums:
            cur, pre = max(num + pre, cur), cur

        return cur





