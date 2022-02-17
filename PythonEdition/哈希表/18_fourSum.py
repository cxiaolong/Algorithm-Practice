from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total > target:
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 0, -1, 0, -2, 2]
    target1 = 0
    nums2 = [2, 2, 2, 2, 2]
    target2 = 8
    print(s.fourSum(nums1, target1))
    print(s.fourSum(nums2, target2))