# 方法1-
class Solution1:
    def integerBreak(self, n: int) -> int:
        # dp[i]表示整数i拆分的整数的积的最大和
        # i可以拆分成j和i-j，i-j不再继续拆分
        # i可以拆分成j和i-j，i-j再继续拆分
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(1, i - 1):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]


if __name__ == '__main__':
    n1 = 2
    n2 = 10
    s1 = Solution1()
    print(s1.integerBreak(n1))
    print(s1.integerBreak(n2))
