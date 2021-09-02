

"""


"""


class Solution(object):

    def longestCommonSubsequence(self, text1, text2):

        """
        状态表示： 定义 f[i][j]表示字符串text1的[1,i]区间和字符串text2的[1,j]区间的最长公共子序列长度（下标从1开始）。

        状态计算：

        可以根据text1[i]和text2[j]的情况，分为两种决策：

                1、若text1[i] == text2[j] ，也就是说两个字符串的最后一位相等，
                    那么问题就转化成了字符串text1的[1,j-1]区间和字符串text2的[1,j-1]区间的最长公共子序列长度再加上一，
                    即f[i][j] = f[i - 1][j - 1] + 1。（下标从1开始）

                2、若text1[i] != text2[j]，也就是说两个字符串的最后一位不相等，
                    那么字符串text1的[1,i]区间和字符串text2的[1,j]区间的最长公共子序列长度无法延长，
                    因此f[i][j]就会继承f[i-1][j]与f[i][j-1]中的较大值，即f[i][j] = max(f[i - 1][j],f[i][j - 1]) 。 （ 下标从1开始）

                因此，状态转移方程为：

                    f[i][j] = f[i-1][j-1] + 1 ,当text1[i] == text2[j]。

                    f[i][j] = max(f[i - 1][j],f[i][j - 1])，当text1[i] != text2[j]​ 。


        时间复杂度: O(mn)

        空间复杂度: O(mn)

        """

        n = len(text1)
        m = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # 声明大小为 (n+1, m+1) 的二维数组
        for i in range(1, m+1):   # 注意二位数组的行列顺序与遍历的顺序
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[m][n]


if __name__ == '__main__':
    a = 'abscdessd'
    b = 'sddcdessf'
    res = Solution().longestCommonSubsequence(a, b)
    print(res)