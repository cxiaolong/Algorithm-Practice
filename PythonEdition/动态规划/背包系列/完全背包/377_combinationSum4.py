from typing import List


# 背包系列
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for j in nums:
                if i >= j:
                    dp[i] += dp[i - j]
        return dp[target]


if __name__ == '__main__':
    nums1 = [1, 2, 3]
    target1 = 4
    nums2 = [9]
    target2 = 3
    s = Solution()
    print(s.combinationSum4(nums1, target1))
    print(s.combinationSum4(nums2, target2))
