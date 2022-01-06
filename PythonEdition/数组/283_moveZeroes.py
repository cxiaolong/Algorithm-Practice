from typing import List

# 方法1-双指针法-左侧指针指向已经处理好的序列的尾部，右侧指针指向待处理序列的头部
class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        左指针左边均为非0数
        左指针与右指针之间均为0
        """
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        return nums


if __name__ == '__main__':
    nums1 = [0, 1, 0, 3, 12]
    nums2 = [0]
    s1 = Solution1()
    print(s1.moveZeroes(nums1))
    print(s1.moveZeroes(nums2))