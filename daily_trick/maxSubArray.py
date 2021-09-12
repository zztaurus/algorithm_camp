
"""

https://leetcode-cn.com/problems/maximum-subarray/

最大子序和

"""


class Solution(object):

    def maxSubArray(self, nums):

        """

        动态规划法

        状态转移方程为：

            dp_i = dp_i-1 + nums[i] if dp_i-1 > 0
            dp_i = nums[i] if dp_i-1 <= 0

            dp[i] = max(num, (dp[i-1] + num))

            最大子序和 = 当前自身元素最大 或者 包含之前后最大

        时间复杂度: O(n)

        空间复杂度: O(1)



        """

        ans = nums[0]
        dp_i = 0  # 表示序列为 【0， i】位置的最大子序和
        for num in nums:
            dp_i = max(dp_i + num, num)
            ans = max(ans, dp_i)  # 本质上是去 max(dp_i, dp_i+1, dp_i+2, dp_i+3. ..... dp_i+n)
        return ans

    def maxSubArray_2(self):
        """

        分治法

        """


if __name__ == '__main__':
    Solution().maxSubArray([1, 2, 3, -7, 3, 4, 56, 77, -96, 2, 5])