
class Solution(object):

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp, p1, p2, p3 = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[p1] * 2, dp[p2] * 3, dp[p3] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2:
                p1 += 1
            if dp[i] == n3:
                p2 += 1
            if dp[i] == n5:
                p3 += 1
        return dp[-1]

