
"""

https://leetcode-cn.com/problems/unique-paths/


62. 不同路径


"""


class Solution(object):

    def uniquePaths(self, m, n):

        """
        动态规划

        状态:
            dp[i][j] 是到达 i, j 最多路径

        转移方程:

            dp[i][j] = dp[i-1][j] + dp[i][j-1]

        注意，对于第一行 dp[0][j]，或者第一列 dp[i][0]，由于都是在边界，所以只能为 1

        初始化dp数组

        1 1 1
        1 0 0


        """

        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    def uniquePaths_1(self, m, n):
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j - 1]
            pre = cur[:]
        return pre[-1]

    def uniquePaths_2(self, m, n):
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j - 1]
            pre = cur[:]
        return pre[-1]
