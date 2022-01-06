from typing import List

# 方法1-动态规划
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        dp = [nums[0] for _ in range(len(nums))]  # dp[i]保存nums[i]处最大连续字串和
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            max_sum = max(max_sum, dp[i])
        return max_sum




if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s1 = Solution1()

    print(s1.maxSubArray(nums))
