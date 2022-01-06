from typing import List


# 方法1
class Solution1:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])
        res1 = self.rob_range(nums, 0, n - 2)
        res2 = self.rob_range(nums, 1, n - 1)
        return max(res1, res2)

    def rob_range(self, nums, start, end):
        if start == end:
            return nums[start]
        dp = [0] * len(nums)
        dp[start] = nums[start]
        dp[start + 1] = max(nums[start], nums[start + 1])
        for i in range(start + 2, end + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[end]


if __name__ == '__main__':
    nums1 = [2, 3, 2]
    nums2 = [1, 2, 3, 1]
    nums3 = [0]
    s1 = Solution1()
    print(s1.rob(nums1))
    print(s1.rob(nums2))
    print(s1.rob(nums3))
