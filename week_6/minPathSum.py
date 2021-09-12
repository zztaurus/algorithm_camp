
"""

https://leetcode-cn.com/problems/minimum-path-sum/

最小路径和

"""


class Solution(object):

    def minPathSum(self, grid):

        """
        动态规划


        状态定义：

            dp[i][j] 表示移动到grid[i][j] 位置的最短路径和



        状态转移方程:


            1) 当前位置不在左边界，也不再上边界
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            2) 当前位置在左边界
                dp[i][j] = dp[i][j-1] + grid[i][j]
            3) 当前位置在上边界:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            4) 当前位置既在上边界，也在左边界
                dp[i][j] = grid[i][j]

            不需要建立 dp 矩阵浪费额外空间，直接遍历 grid[i][j]修改即可。这是因为：grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j] ；
            原 grid 矩阵元素中被覆盖为dp元素后（都处于当前遍历点的左上方），不会再被使用到。


        时间复杂度: O(m * n) 遍历矩阵中的每个元素
        空间复杂度: O(1) 直接修改原矩阵，不使用额外空间。

        """
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == j == 0: continue
                elif i == 0 and j > 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                elif i > 0 and j == 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j-1]) + grid[i][j]

        return grid[m-1][n-1]



