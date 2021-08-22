
"""

https://leetcode-cn.com/problems/get-kth-magic-number-lcci/


面试题 17.09. 第 k 个数

"""

import heapq


class Solution(object):

    def getKthMagicNumber(self, k):
        """

        三指针法
        """

        dp, p1, p2, p3 = [1] * k, 0, 0, 0
        for i in range(1, k):
            n2, n3, n5 = dp[p1] * 3, dp[p2] * 5, dp[p3] * 7
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2:
                p1 += 1
            if dp[i] == n3:
                p2 += 1
            if dp[i] == n5:
                p3 += 1
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    res = s.getKthMagicNumber(5)
    print(res)

