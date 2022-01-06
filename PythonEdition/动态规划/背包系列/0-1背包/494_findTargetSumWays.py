from typing import List


# 方法1-回溯算法
class Solution1:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def back_track(nums, target, sum, start):
            if sum == target:
                res.append(path.copy())
            elif sum > target:
                return
            else:
                for i in range(start, len(nums)):
                    sum += nums[i]
                    path.append(nums[i])
                    back_track(nums, target, sum, i + 1)
                    sum -= nums[i]
                    path.pop()

        res = []
        path = []
        if target > sum(nums):
            return 0
        if (target + sum(nums)) % 2:
            return 0
        nums.sort()
        bag_size = (target + sum(nums)) // 2
        back_track(nums, bag_size, 0, 0)
        return len(res)


# 方法二-转化为01背包问题
class Solution2:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_nums = sum(nums)
        if (target + sum_nums) % 2 or target > sum_nums:
            return 0
        bag_size = (target + sum_nums) // 2
        bag_size = bag_size if bag_size > 0 else -bag_size  # 保证背包容量是个正数
        dp = [0] * (bag_size + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(bag_size, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[bag_size]


if __name__ == '__main__':
    nums1 = [1, 1, 1, 1, 1]
    target1 = 3
    nums2 = [1]
    target2 = 1
    nums3 = [100]
    target3 = -200
    s1 = Solution1()
    s2 = Solution2()
    # print(s2.findTargetSumWays(nums1, target1))
    # print(s2.findTargetSumWays(nums2, target2))
    print(s2.findTargetSumWays(nums3, target3))
