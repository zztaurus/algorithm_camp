
"""


https://leetcode-cn.com/problems/triangle/

三角形最小路径和

"""


class Solution(object):

    def minimumTotal(self, triangle):



        if not triangle:
            return
        res = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
        return res[0]

    # Modify the original triangle, bottom-up
    def minimumTotal3(self, triangle):

        """

          动态规划

          dp[i][j] 表示从点 (i, j) 到底边的最小路径和。

          dp[i][j]= min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]

          bottom - top

          时间复杂度: O(n^2)

          空间复杂度: O(n)

        """

        if not triangle:
            return
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1]) # 三角形 (j, j + 1, j + 2, j + 3, 从上到下 j 递增)
        return triangle[0][0]

    # Modify the original triangle, top-down
    def minimumTotal2(self, triangle):
        if not triangle:
            return
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        return min(triangle[-1])

    def minimumTotal1(self, triangle):
        if not triangle:
            return
        res = [[0 for i in range(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    res[i][j] = res[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    res[i][j] = res[i - 1][j - 1] + triangle[i][j]
                else:
                    res[i][j] = min(res[i - 1][j - 1], res[i - 1][j]) + triangle[i][j]
        return min(res[-1])






