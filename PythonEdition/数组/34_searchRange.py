from typing import List


# 方法1
class Solution1:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)
        cur_pos = -1
        while l < r:
            mid = l + (r - l) // 2
            if target < nums[mid]:
                r = mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                cur_pos = mid
                break
        if cur_pos == -1:
            return [-1, -1]
        for i in range(cur_pos, -1, -1):
            if nums[i] < target:
                start = i+1
                break
        for j in range(cur_pos-1, len(nums)):
            if nums[j] > target:
                end = j-1
                break
        return [start, end]


# 方法2-二分法思想很简单，细节是魔鬼
class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return l
        a = find_left(nums, target)
        b = find_left(nums, target + 1)
        if a == len(nums) or nums[a] != target:
            return [-1, -1]
        else:
            return [a, b - 1]




if __name__ == '__main__':
    nums1 = [5, 7, 7, 8, 8, 10]
    target1 = 8
    nums2 = [5, 7, 7, 8, 8, 10]
    target2 = 6
    nums3 = []
    target3 = 0
    s1 = Solution1()
    s2 = Solution2()
    print(s1.searchRange(nums1, target1))
    print(s1.searchRange(nums2, target2))
    print(s1.searchRange(nums3, target3))
    print(s2.searchRange(nums1, target1))
    print(s2.searchRange(nums2, target2))
    print(s2.searchRange(nums3, target3))
