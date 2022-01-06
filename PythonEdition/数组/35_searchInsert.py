from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            middle = l + (r - l) // 2
            if target < nums[middle]:
                r = middle - 1
            elif target > nums[middle]:
                l = middle + 1
            else:
                return middle
        return l


if __name__ == '__main__':
    nums1 = [1, 3, 5, 6]
    target1 = 5
    nums2 = [1, 3, 5, 6]
    target2 = 2
    nums3 = [1, 3, 5, 6]
    target3 = 7
    s = Solution()
    print(s.searchInsert(nums1, target1))
    print(s.searchInsert(nums2, target2))
    print(s.searchInsert(nums3, target3))