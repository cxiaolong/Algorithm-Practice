from typing import List


# 完全背包
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[amount] if dp[amount] <= amount else -1


if __name__ == '__main__':
    coins1 = [1, 2, 5]
    amount1 = 11
    coins2 = [2]
    amount2 = 3
    coins3 = [1]
    amount3 = 0
    coins4 = [1]
    amount4 = 1
    coins5 = [1]
    amount5 = 2
    s = Solution()
    print(s.coinChange(coins1, amount1))
    print(s.coinChange(coins2, amount2))
    print(s.coinChange(coins3, amount3))
    print(s.coinChange(coins4, amount4))
    print(s.coinChange(coins5, amount5))
