# 方法1-动态规划
class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1、明确dp数组的含义
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # 2、初始化dp数组
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        # 3、遍历
        for i in range(1, m):
            for j in range(1, n):
                # 4、写出dp表达式
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


# 方法2-组合数
# class Solution2:
#     def uniquePath(self, m: int, n: int) -> int:
#         return comb(m+n-2, n-1)


if __name__ == '__main__':
    s1 = Solution1()
    m, n = 3, 7
    # s2 = Solution2()
    print(s1.uniquePaths(3, 7))
    # s2.uniquePath(3, 7)