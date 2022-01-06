from typing import List


# 方法1-暴力解法：搜索出所有连续子数组，求所有子数组的和，取最大值
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        pass


# 方法2-贪心算法
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        s = len(nums)
        if s != 1:
            for i in range(1, s):
                max_sum = max(nums[i], max_sum + nums[i])
        return max_sum


# 方法3-动态规划
class Solution3:
    def maxSubArray(self, nums: List[int]) -> int:
        pass


if __name__ == '__main__':
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums2 = [1]
    nums3 = [0]
    nums4 = [-1]
    nums5 = [-100000]
    s1 = Solution1()
    s2 = Solution2()
    s3 = Solution3()
    print(s1.maxSubArray(nums1))
    print(s1.maxSubArray(nums2))
    print(s1.maxSubArray(nums3))
    print(s1.maxSubArray(nums4))
    print(s1.maxSubArray(nums5))
    print(s2.maxSubArray(nums1))
    print(s2.maxSubArray(nums2))
    print(s2.maxSubArray(nums3))
    print(s2.maxSubArray(nums4))
    print(s2.maxSubArray(nums5))
