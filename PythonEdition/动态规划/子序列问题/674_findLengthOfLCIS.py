from typing import List


# 方法1-贪心算法
class Solution1:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        pass


# 方法2-动态规划
class Solution2:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        res = 1
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                dp[i + 1] = dp[i] + 1
            res = max(res, dp[i + 1])
        return res


if __name__ == '__main__':
    nums1 = [1, 3, 5, 4, 7]
    nums2 = [2, 2, 2, 2, 2]
    s1 = Solution1()
    s2 = Solution2()
    print(s2.findLengthOfLCIS(nums1))
    print(s2.findLengthOfLCIS(nums2))
