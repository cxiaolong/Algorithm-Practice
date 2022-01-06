from typing import List


# 方法1-贪心算法
class Solution1:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        preC, curC, res = 0, 0, 1
        for i in range(len(nums) - 1):
            curC = nums[i + 1] - nums[i]
            if curC * preC <= 0 and curC != 0:
                res += 1
                preC = curC
        return res


# 方法2-动态规划
class Solution2:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        pass


if __name__ == '__main__':
    nums1 = [1, 7, 4, 9, 2, 5]
    nums2 = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
    nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    s1 = Solution1()
    s2 = Solution2()
    print(s1.wiggleMaxLength(nums1))
    print(s1.wiggleMaxLength(nums2))
    print(s1.wiggleMaxLength(nums3))
