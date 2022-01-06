# 方法1-递归
class Solution1:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n-2)


# 方法2-动态规划
class Solution2:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


if __name__ == '__main__':
    s1 = Solution1()
    s2 = Solution2()
    print(s1.climbStairs(4))
    print(s2.climbStairs(4))
