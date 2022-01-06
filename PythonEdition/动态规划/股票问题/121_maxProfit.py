from typing import List


# 方法1-贪心算法（一次遍历）: 边遍历边记录股票价格的最小值和利润的最大值
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:  # 依次遍历每天的股票价格
            min_price = min(min_price, price)
            max_profit = max(max_profit, price-min_price)

        return max_profit


# 动态规划
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        # dp[i]表示前i天买卖股票获得的最大利润
        dp = [0 for _ in range(n)]
        min_price = prices[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1], prices[i]-min_price)
            if prices[i] < min_price:
                min_price = prices[i]
        return dp[-1]



if __name__ == '__main__':
    prices1 = [7, 1, 5, 3, 6, 4]
    prices2 = [7, 6, 4, 3, 1]
    prices3 = [4]
    s1 = Solution1()
    s2 = Solution2()
    print(s2.maxProfit(prices1))
    print(s2.maxProfit(prices2))
    print(s2.maxProfit(prices3))
