from typing import List


# 方法1-暴力解法
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# 方法2-哈希表
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target-num], i]
            hashtable[num] = i
        return []


if __name__ == '__main__':
    nums1 = [2, 7, 11, 15]
    target1 = 9

    nums2 = [3, 2, 4]
    target2 = 6

    nums3 = [3, 3]
    target3 = 6

    s1 = Solution1()
    print(s1.twoSum(nums1, target1))
    print(s1.twoSum(nums2, target2))
    print(s1.twoSum(nums3, target3))

    s2 = Solution2()
    print(s2.twoSum(nums1, target1))
    print(s2.twoSum(nums2, target2))
    print(s2.twoSum(nums3, target3))