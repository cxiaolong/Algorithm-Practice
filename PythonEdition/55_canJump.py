from typing import List


# 贪心算法-遍历的时候，记录每次可以跳到的最远位置
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_i = nums[0]  # max_i表示当前所能到达到的最远距离
        size = len(nums)
        if size == 1:
            return True
        for i in range(1, size):
            if max_i < i: return False
            max_i = max(i + nums[i], max_i)
            if max_i >= size-1: return True

class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        max_i = nums[0]  # 记录所能跳到的最远位置
        size = len(nums)
        if size == 1:
            return True
        for i in range(size):
            if max_i < i:
                return False
            max_i = max(max_i, nums[i]+i)
            if max_i >= size - 1:
                return True


if __name__ == '__main__':
    nums1 = [2, 3, 1, 1, 4]
    nums2 = [3, 2, 1, 0, 4]
    s = Solution2()
    print(s.canJump(nums1))
    print(s.canJump(nums2))
