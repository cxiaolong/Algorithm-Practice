from typing import List


# 双指针法
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()

        for i in range(n):  # 去重，a需要和上次枚举的不同
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1  # 右指针左移
                elif total < 0:
                    left += 1   # 左指针右移
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:  # 去重，确保下次枚举的b与这次不同
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:  # 去重，确保下次枚举的c与这次不同
                        right -= 1
                    left += 1
                    right -= 1
        return res


if __name__ == '__main__':
    nums1 = [-1, 0, 1, 2, -1, -4]
    nums2 = []
    nums3 = [0]
    s = Solution()
    print(s.threeSum(nums1))
    print(s.threeSum(nums2))
    print(s.threeSum(nums3))