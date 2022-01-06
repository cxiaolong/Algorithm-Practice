from typing import List


# 方法1-双指针：将不等于val的数值全部移到前面
class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1
        return idx, nums


# 方法2-双指针优化：从尾向头遍历（避免了元素的重复赋值操作)
class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left, nums


if __name__ == '__main__':
    nums1 = [3, 2, 2, 3]
    val1 = 3
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    s1 = Solution1()
    s2 = Solution2()
    # print(s1.removeElement(nums1, val1))
    # print(s1.removeElement(nums2, val2))
    print(s2.removeElement(nums1, val1))
    print(s2.removeElement(nums2, val2))
