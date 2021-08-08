class ClimbStair(object):

    dp = {1: 1, 2: 2}

    def solution_1(self, n):

        """
        :param n:
        :return:

        动态规划，因为重复计算的问题会导致超时
        """
        if n == 0 or n == 1:
            return 1
        return self.solution_1(n - 1) + self.solution_1(n - 2)

    def solution_2(self, n):
        """
        :type n: int
        :rtype: int

        记忆化递归

        """

        if n not in self.dp:
            self.dp[n] = self.solution_2(n - 1) + self.solution_2(n - 2)
        return self.dp[n]

    def solution_3(self, n) -> int:

        """

        :param n:
        :return:

        动态规划
        """

        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

    def solution_4(self, n):

        """
        核心思想: 找到重复子问题, 把复杂问题简单化
        f(n)只依赖于f(n-1)和f(n-2)，只需要两项就足够了, 所以可以省略 dp数组，优化时间负载度为 O(1)
        """

        a = b = 1
        for i in range(2, n + 1):
            a, b = b, a + b

        return b





