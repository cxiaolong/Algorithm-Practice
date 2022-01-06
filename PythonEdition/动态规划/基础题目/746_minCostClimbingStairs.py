from typing import List


# 方法1-动态规划
class Solution1:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        dp[1] = cost[0]
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[-1]



if __name__ == '__main__':
    cost1 = [10, 15, 20]
    cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    s1 = Solution1()
    print(s1.minCostClimbingStairs(cost1))
    print(s1.minCostClimbingStairs(cost2))