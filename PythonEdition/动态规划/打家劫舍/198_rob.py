from typing import List


# 动态规划
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = nums[0] if nums[0] > nums[1] else nums[1]
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]


if __name__ == '__main__':
    nums1 = [1, 2, 3, 1]
    nums2 = [2, 7, 9, 3, 1]
    s = Solution()
    print(s.rob(nums1))
    print(s.rob(nums2))
