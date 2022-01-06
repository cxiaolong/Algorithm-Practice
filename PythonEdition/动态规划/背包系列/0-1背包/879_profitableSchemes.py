from typing import List


# 0-1背包问题
# 本题与经典背包问题非常相似。两者不同在于经典背包问题只有一种容量限制，而本题却有两种限制：集团员工上限n，以及工作产生的利润下限minProfit
class Solution1:
    # 采用动态规划（0-1背包求解）
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        # 本题中的动态数组有两种定义（理解）方式，对应于两种边界条件（初始化），因此返回形式不同
        # 定义1：dp[i][j][k]定义为前i个工作中恰好选择j个员工，并且满足工作利润至少为k的情况下的盈利计划的总数目
        # 按照定义1，初始化为dp[0][0][0] = 1，返回的结果是累加和
        # 定义2：dp[i][j][k]定义为前i个工作中最多选择j个员工，并且满足工作利润至少为k的情况下的盈利计划的总数目
        # 按照定义2，初始化dp[0][j][0] = 1，直接返回dp[len][n][profit]
        MOD = 10 ** 9 + 7
        length = len(group)
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(length + 1)]
        dp[0][0][0] = 1  # 第一种定义方式
        for i in range(1, length + 1):
            members, earn = group[i - 1], profit[i - 1]
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    if j < members:
                        dp[i][j][k] = dp[i - 1][j][k]
                    else:
                        dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - members][max(0, k - earn)]
        total = sum(dp[length][j][minProfit] for j in range(n + 1)) % MOD
        return total


# 空间优化
class Solution2:
    # 采用动态规划（0-1背包求解）
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        # 可以发现dp[i][j][k]仅与dp[i-1][...][...]有关，因此本题可以考虑空间优化，转化为二维数组解决
        # dp[i][j]表示为最多选择i个员工并且满足工作利润至少为j的情况下的盈利计划的数量
        MOD = 10 ** 9 + 7
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1  # 这里使用dp数组的第二种定义方式
        for members, earn in zip(group, profit):
            for i in range(n, members - 1, -1):
                for j in range(minProfit, - 1, -1):  # 利润最低是0
                    dp[i][j] += dp[i - members][max(0, j - earn)]
        return dp[n][minProfit] % MOD


if __name__ == '__main__':
    n1 = 5
    minProfit1 = 3
    group1 = [2, 2]
    profit1 = [2, 3]
    n2 = 10
    minProfit2 = 5
    group2 = [2, 3, 5]
    profit2 = [6, 7, 8]
    s1 = Solution1()
    s2 = Solution2()
    print(s1.profitableSchemes(n1, minProfit1, group1, profit1))
    print(s1.profitableSchemes(n2, minProfit2, group2, profit2))
    print(s2.profitableSchemes(n1, minProfit1, group1, profit1))
    print(s2.profitableSchemes(n2, minProfit2, group2, profit2))
