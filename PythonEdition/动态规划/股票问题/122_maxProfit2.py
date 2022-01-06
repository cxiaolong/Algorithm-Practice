from typing import List


# 方法1-贪心算法：只要股票今天的价格比明天的低，今天就买入股票，明天卖出，依次遍历
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        profits = 0
        n = len(prices)
        if n > 1:
            for i in range(1, n):
                profit = prices[i] - prices[i - 1]
                if profit > 0:
                    profits += profit
        return profits


# 方法2-动态规划
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1 or n == 0: return 0
        dp = [0] * len(prices)
        for i in range(1, n):
            if prices[i] - prices[i - 1] > 0:
                # 你必须在再次购买前出售掉之前的股票（换一种思考方式：即相当于我当天没卖，等到下一次再卖，与当天买卖实际是相同的）
                dp[i] = dp[i - 1] + prices[i] - prices[i - 1]
            else:
                dp[i] = dp[i - 1]
        return dp[n-1]


# 方法3-动态规划
class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][0]表示第i天持有股票获得的最大利润
        # dp[i][1]表示第i天不持有股票获得的最大利润
        n = len(prices)
        if n == 1: return 0
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        return dp[-1][1]


if __name__ == '__main__':
    prices1 = [7, 1, 5, 3, 6, 4]
    prices2 = [1, 2, 3, 4, 5]
    prices3 = [7, 6, 4, 3, 1]
    s1 = Solution1()
    s2 = Solution2()
    s3 = Solution3()
    print(s1.maxProfit(prices1))
    print(s1.maxProfit(prices2))
    print(s1.maxProfit(prices3))
    print(s2.maxProfit(prices1))
    print(s2.maxProfit(prices2))
    print(s2.maxProfit(prices3))
    print(s3.maxProfit(prices1))
    print(s3.maxProfit(prices2))
    print(s3.maxProfit(prices3))