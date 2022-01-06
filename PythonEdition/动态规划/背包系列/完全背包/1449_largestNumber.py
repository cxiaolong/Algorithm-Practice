from typing import List


# 方法一：动态规划（二维完全背包）
class Solution1:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # 若两个整数位数不同，位数更多的整数必然大于位数小的整数。因此我们需要先计算出可以得到的整数的最大位数
        # 在计算最大位数的同时，记录下每次状态转移的来源
        # dp[i][j]定义为前i个位数，构成成本恰好为j的的最大位数
        dp = [[float("-inf")] * (target + 1) for _ in range(10)]
        dp[0][0] = 0
        where = [[0] * (target + 1) for _ in range(10)]
        for i, c in enumerate(cost):
            for j in range(target + 1):
                if j < c:
                    dp[i + 1][j] = dp[i][j]
                    where[i + 1][j] = j
                else:
                    if dp[i][j] > dp[i + 1][j - c] + 1:
                        dp[i + 1][j] = dp[i][j]
                        where[i + 1][j] = j
                    else:
                        dp[i + 1][j] = dp[i + 1][j - c] + 1
                        where[i + 1][j] = j - c
        if dp[9][target] < 0:
            return "0"

        ans = list()
        i, j = 9, target
        while i > 0:
            if j == where[i][j]:
                i -= 1
            else:
                ans.append(str(i))
                j = where[i][j]
        return "".join(ans)


# 方法2：空间优化
# 时间复杂度O(n*target)，空间复杂度O(target)
class Solution2:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # 优化1：滚动数组
        # 优化2：去掉from数组（当选择了第i位数字时，dp[j]==dp[j-cost[i]+1]
        # dp[i]表示恰好能构成成本i的最大位数长度
        dp = [float("-inf")] * (target + 1)
        dp[0] = 0
        for c in cost:
            for i in range(c, target + 1):
                dp[i] = max(dp[i], dp[i - c] + 1)
        if dp[target] < 0:
            return "0"
        ans = list()
        j = target
        for i in range(8, -1, -1):
            c = cost[i]
            while j >= c and dp[j] == dp[j - c] + 1:
                ans.append(str(i + 1))
                j -= c
        return "".join(ans)


# 方法3：直接比较大小（使用支持大整数的语言）
class Solution3:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # dp[i]表示前i个位数恰好可以组成总成本为target的最大位数
        dp = [0] + [float("-inf")] * target
        for i in range(8, -1, -1):
            for j in range(cost[i], target + 1):
                dp[j] = max(dp[j], dp[j - cost[i]] * 10 + i + 1)
        return str(dp[target]) if dp[target] >= 0 else "0"


if __name__ == '__main__':
    cost1 = [4, 3, 2, 5, 6, 7, 2, 5, 5]
    target1 = 9
    cost2 = [7, 6, 5, 5, 5, 6, 8, 7, 8]
    target2 = 12
    cost3 = [6, 10, 15, 40, 40, 40, 40, 40, 40]
    target3 = 47
    cost4 = [2, 4, 6, 2, 4, 6, 4, 4, 4]
    target4 = 5
    s1 = Solution1()
    s2 = Solution2()
    s3 = Solution3()
    print(s1.largestNumber(cost1, target1))
    print(s1.largestNumber(cost2, target2))
    print(s1.largestNumber(cost3, target3))
    print(s1.largestNumber(cost4, target4))
    print(s2.largestNumber(cost1, target1))
    print(s2.largestNumber(cost2, target2))
    print(s2.largestNumber(cost3, target3))
    print(s2.largestNumber(cost4, target4))
    print(s3.largestNumber(cost1, target1))
    print(s3.largestNumber(cost2, target2))
    print(s3.largestNumber(cost3, target3))
    print(s3.largestNumber(cost4, target4))
