from typing import List


# 贪心算法-法1
class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0  # 当前所能覆盖的最远距离
        max_distance = len(nums) - 1  # 最远距离的下标
        if max_distance == 0:
            return True
        for i in range(len(nums)):
            cover = max(cover, i + nums[i])
            if cover >= max_distance:
                return True
            if cover <= i:
                return False


# 贪心算法-法2
class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        distance = len(nums) - 1  # 最远距离的下标
        max_i = 0  # 下标为i的地方所能达到的最远距离，初始化为0
        for i, jump in enumerate(nums):  #i为当前位置，jump是当前位置可以跳跃的距离
            if max_i < i:
                return False
            max_i = max(max_i, i+jump)
            if max_i >= distance:
                return True



if __name__ == '__main__':
    nums1 = [2, 3, 1, 1, 4]
    nums2 = [3, 2, 1, 0, 4]
    s1 = Solution1()
    s2 = Solution2()
    print(s1.canJump(nums1))
    print(s1.canJump(nums2))
    print(s2.canJump(nums1))
    print(s2.canJump(nums2))