from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum_weight = sum(stones)
        target = sum_weight // 2
        dp = [0] * (target+1)
        for i in range(len(stones)):
            for j in range(target, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]]+stones[i])
        return sum_weight - 2 * dp[target]


if __name__ == '__main__':
    stones1 = [2, 7, 4, 1, 8, 1]
    stones2 = [31, 26, 33, 21, 40]
    stones3 = [1, 2]
    s = Solution()
    print(s.lastStoneWeightII(stones1))
    print(s.lastStoneWeightII(stones2))
    print(s.lastStoneWeightII(stones3))
