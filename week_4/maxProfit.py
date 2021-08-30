"""

https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/

买卖股票的最佳时机 II

"""


class Solution(object):

    def maxProfit(self, prices):

        """
        动态规划

        转移方程: 第i天的收益依赖于第i-1天的收益。

        时间复杂度: O(n)
        空间复杂度: O(n)

        """

        n = len(prices)
        if n < 2:
            return 0
        cash = []
        hold = []
        cash.append(0)   # 第一天不持有的收益
        hold.append(-prices[0])  # 第一天持有的收益
        for i in range(1, n):
            cash.append(max(cash[i - 1], hold[i - 1] + prices[i]))  # 第i天不持有的收益
            hold.append(max(hold[i - 1], cash[i - 1] - prices[i]))  # 第i天持有的收益

        return cash[n-1]

    def maxProfit_2(self, prices):

        """

        动态规划代码优化

        """

        n = len(prices)
        if n < 2:
            return 0
        pre_cash = 0
        pre_hold = -prices[0]
        for i in range(1, n):
            cash = max(pre_cash, pre_hold + prices[i])
            hold = max(pre_hold, pre_cash - prices[i])

            pre_cash = cash
            pre_hold = hold

        return pre_cash

    def maxProfit_3(self, prices):

        """

        贪心算法

        每次选择当前看起来最佳的选择，做出局部最优的选择，然后通过局部最优解得到全局最优解。


        """

        n = len(prices)
        if n < 2:
            return 0

        res = 0

        for i in range(1, n):
            profit = prices[i] - prices[i-1]
            if profit > 0:
                res += profit