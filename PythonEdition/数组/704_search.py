from typing import List


# 版本1-左闭右闭区间
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            middle = (l + r) // 2
            if nums[middle] == target:
                return middle
            if target < nums[middle]:
                r = middle - 1
            elif target > nums[middle]:
                l = middle + 1
        return -1


# 版本2-左闭右开区间
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            middle = (l + r) // 2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                r = middle
            elif target > nums[middle]:
                l = middle + 1
        return -1


# 方法3-递归
class Solution3:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, target, l, r):
            if l > r:
                return -1
            middle = r + (l - r) // 2
            if target < nums[middle]:
                return binary_search(nums, target, l, middle - 1)
            elif target > nums[middle]:
                return binary_search(nums, target, middle + 1, r)
            else:
                return middle

        res = binary_search(nums, target, 0, len(nums) - 1)
        return res


if __name__ == '__main__':
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    s1 = Solution1()
    s2 = Solution2()
    s3 = Solution3()
    print(s1.search(nums1, target1))
    print(s1.search(nums2, target2))
    print(s2.search(nums1, target1))
    print(s2.search(nums2, target2))
    print(s3.search(nums1, target1))
    print(s3.search(nums2, target2))
