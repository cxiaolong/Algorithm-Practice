from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i]表示i（包括）之前的最长子序列长度
        result = 0
        size = len(nums)
        if size != 0:
            dp = [1] * size
            for i in range(1, size):
                for j in range(i):
                    if nums[i] > nums[j]:
                        dp[i] = max(dp[i], dp[j] + 1)
                result = max(result, dp[i])
        return result


if __name__ == '__main__':
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    nums2 = [0, 1, 0, 3, 2, 3]
    nums3 = [7, 7, 7, 7, 7, 7, 7]
    s = Solution()
    print(s.lengthOfLIS(nums1))
    print(s.lengthOfLIS(nums2))
    print(s.lengthOfLIS(nums3))
