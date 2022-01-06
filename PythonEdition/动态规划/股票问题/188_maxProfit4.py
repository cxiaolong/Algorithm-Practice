from typing import List


class Solution1:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 动态数组dp[i][j]定义为第i天所能获得的最大利润，其中k表示第i天所处的状态
        n = len(prices)
        if n == 1: return 0
        dp = [[0] * (2 * k + 1) for _ in range(n)]
        for k in range(1, 2 * k, 2):
            dp[0][k] = -prices[0]
        for i in range(1, n):
            for j in range(0, 2 * k - 1, 2):
                dp[i][j + 1] = max(dp[i - 1][j + 1], dp[i - 1][j] - prices[i])
                dp[i][j + 2] = max(dp[i - 1][j + 2], dp[i - 1][j + 1] + prices[i])
        return dp[-1][2 * k]


if __name__ == '__main__':
    k1 = 2
    prices1 = [2, 4, 1]
    k2 = 2
    prices2 = [3, 2, 6, 5, 0, 3]
    s1 = Solution1()
    print(s1.maxProfit(k1, prices1))
    print(s1.maxProfit(k2, prices2))
