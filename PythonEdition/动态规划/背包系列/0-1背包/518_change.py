from typing import List


class Solution1:
    def change(self, amount: int, coins: List[int]) -> int:
        length = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(length):
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j-coins[i]]
        return dp[amount]


if __name__ == '__main__':
    amount1 = 5
    coins1 = [1, 2, 5]
    amount2 = 3
    coins2 = [2]
    amount3 = 10
    coins3 = [10]
    s = Solution1()
    print(s.change(amount1, coins1))
    print(s.change(amount2, coins2))
    print(s.change(amount3, coins3))
