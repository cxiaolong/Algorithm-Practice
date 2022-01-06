from typing import List


# 方法1-01背包二重数组
class Solution1:
    # 1、明确dp数组及其下标含义：dp[i][j]表示能否从数组的[0-i]下标范围内选取出若干数恰好和为j
    # 2、状态转移方程：j<nums[i]时，dp[i][j]=dp[i-1][j]，j>=nums[i]时，dp[i][j]=dp[i-1][j-nums[i]] ｜ dp[i-1][j]
    # 3、初始化dp数组：dp[i][0]=True, dp[0][nums[0]]=True
    def canPartition(self, nums: List[int]) -> bool:
        length = len(nums)
        total = sum(nums)
        max_num = max(nums)
        if length < 2:
            return False
        if total % 2:
            return False
        target = total // 2
        if max_num > target:
            return False
        dp = [[False] * (target + 1) for _ in range(length)]
        for i in range(length):
            dp[i][0] = True
        dp[0][nums[0]] = True

        for i in range(1, length):
            for j in range(1, target + 1):
                if j < nums[i]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i]]
        return dp[length - 1][target]


# 方法1-01背包空间优化
class Solution2:
    # 1、明确dp数组及其下标含义：dp[j]表示能否从数组中选取出若干数恰好和为j
    # 2、状态转移方程：dp[j] ｜= dp[j-nums[i]]
    # 3、初始化dp数组：dp[0]=True
    def canPartition(self, nums: List[int]) -> bool:
        length = len(nums)
        total = sum(nums)
        max_num = max(nums)
        if length < 2:
            return False
        if total % 2:
            return False
        target = total // 2
        if max_num > target:
            return False
        dp = [True] + [False] * target
        for i in range(length):
            for j in range(target, nums[i] - 1, -1):
                dp[j] |= dp[j - nums[i]]
        return dp[target]


# 方法3-直接套用0-1背包
class Solution3:
    def canPartition(self, nums):
        length = len(nums)
        total = sum(nums)
        max_num = max(nums)
        if length < 2:
            return False
        if total % 2:
            return False
        target = total // 2
        if max_num > target:
            return False
        dp = [0] * (target + 1)
        for i in range(length):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        return dp[target] == target


# 方法3-回溯算法
class Solution4:
    def canPartition(self, nums):
        sum_ = sum(nums)
        half = sum_ / 2
        res = []
        if sum_ % 2 == 1:
            return False

        def back_track(nums, path, start_index):
            if sum(path) > half:
                return
            if sum(path) == half:
                res.append(path)
                return
            for i in range(start_index, len(nums)):
                path.append(nums[i])
                back_track(nums, path, i)
                path.pop()
        back_track(nums, [], 0)
        if res:
            return True
        return False


if __name__ == '__main__':
    nums1 = [1, 5, 11, 5]
    nums2 = [1, 2, 3, 5]
    s1 = Solution1()
    s2 = Solution2()
    s3 = Solution3()
    s4 = Solution4()
    print(s1.canPartition(nums1))
    print(s1.canPartition(nums2))
    print(s2.canPartition(nums1))
    print(s2.canPartition(nums2))
    print(s3.canPartition(nums1))
    print(s3.canPartition(nums2))
    print(s4.canPartition(nums1))
    print(s4.canPartition(nums2))
