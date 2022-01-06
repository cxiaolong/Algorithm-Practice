from typing import List


# 方法1-
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][j]表示第i天所能获得的最大利润，j对应以下五种状态
        # 0：没有操作，1：第一次持有，2：第一次卖出，3：第二次持有，4：第二次卖出
        n = len(prices)
        dp = [[0] * 5 for _ in range(n)]
        dp[0][1] = -prices[0]
        dp[0][3] = -prices[0]
        for i in range(1, n):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = max(dp[i-1][1] + prices[i], dp[i-1][2])
            dp[i][3] = max(dp[i-1][2] - prices[i], dp[i-1][3])
            dp[i][4] = max(dp[i-1][3] + prices[i], dp[i-1][4])
        return max(dp[-1])


if __name__ == '__main__':
    prices1 = [3, 3, 5, 0, 0, 3, 1, 4]
    prices2 = [1, 2, 3, 4, 5]
    prices3 = [7, 6, 4, 3, 1]
    prices4 = [1]
    s1 = Solution1()
    print(s1.maxProfit(prices1))
    print(s1.maxProfit(prices2))
    print(s1.maxProfit(prices3))
    print(s1.maxProfit(prices4))
