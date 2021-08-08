class Solution(object):

    dp = {1: 1, 2: 2}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n not in self.dp:
            self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]


    def climbStairs_1(self, n):



