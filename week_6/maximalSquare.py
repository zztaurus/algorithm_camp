

"""

https://leetcode-cn.com/problems/maximal-square/

最大正方形


"""


class Solution(object):

    def maximalSquare(self, matrix):

        """

        暴力法，由大到小, 遍历所有的正方形

        遍历矩阵中的每个元素，每次遇到 11，则将该元素作为正方形的左上角；

        确定正方形的左上角后，根据左上角所在的行和列计算可能的最大正方形的边长（正方形的范围不能超出矩阵的行数和列数），在该边长范围内寻找只包含 11 的最大正方形；

        每次在下方新增一行以及在右方新增一列，判断新增的行和列是否满足所有元素都是 11。


        时间复杂度：O(m*n*min(m,n)^2)，其中 mm 和 nn 是矩阵的行数和列数。

        空间复杂度: O(1)


        """

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    # 遇到一个 1 作为正方形的左上角
                    maxSide = max(maxSide, 1)  # 此时最小的正方形为 1 * 1
                    # 计算可能的最大正方形边长
                    currentMaxSide = min(rows - i, columns - j)
                    for k in range(1, currentMaxSide):
                        # 判断新增的一行一列是否均为 1
                        flag = True
                        if matrix[i + k][j + k] == '0':
                            break
                        for m in range(k):
                            if matrix[i + k][j + m] == '0' or matrix[i + m][j + k] == '0':
                                flag = False
                                break
                        if flag:
                            maxSide = max(maxSide, k + 1)
                        else:
                            break

        maxSquare = maxSide * maxSide
        return maxSquare

    def maximalSquare_2(self, matrix):

        """

        状态定义: dp(i,j) 表示以(i,j) 为右下角，且只包含 1 的正方形的边长最大值。
                如果我们能计算出所有dp(i,j) 的值，那么其中的最大值即为矩阵中只包含 1 的正方形的边长最大值，
                其平方即为最大正方形的面积。

        转移方程:

                dp(i,j)=0，因为当前位置不可能在由 1 组成的正方形中；

                dp(i, j) = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1, 取三者最小 + 1

                如果 i 和 j 中至少有一个为 0，则以位置 ((i,j) 为右下角的最大正方形的边长只能是 1，因此dp(i,j)=1。

        """

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 # 取三者最小 + 1
                    maxSide = max(maxSide, dp[i][j])

        maxSquare = maxSide * maxSide
        return maxSquare
