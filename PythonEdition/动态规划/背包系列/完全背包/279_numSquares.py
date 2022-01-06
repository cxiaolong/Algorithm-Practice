class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(i * i, n + 1):
                dp[j] = min(dp[j], dp[j - i * i] + 1)
        return dp[n]


if __name__ == '__main__':
    n1 = 12
    n2 = 13
    s = Solution()
    print(s.numSquares(n1))
    print(s.numSquares(n2))

