import bisect
from typing import List


# 方法1-暴力法-双重循环
class Solution1:
    """
    time complexity: O(n**2)  在LeetCode上提交没通过
    space complexity: O(1)
    """

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = n + 1
        for i in range(n):
            for j in range(i + 1, n + 1):
                if sum(nums[i:j]) >= target:
                    res = min(res, j - i)
                    break
        return res if res != n + 1 else 0


# 方法2-前缀和+二分查找
class Solution2:
    """
    time complexity: O(nlogn)
    space complexity: O(n)
    """

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        def find_left(nums, s):
            n = len(nums)
            left, right = 0, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if s <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        n = len(nums)
        res = n + 1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])

        for i in range(1, n + 1):
            s = target + sums[i - 1]
            # bound = find_left(sums, s)
            bound = bisect.bisect_left(sums, s)
            if bound != len(sums):
                res = min(res, bound - (i - 1))

        return 0 if res == n + 1 else res


# 方法3-滑动窗口：start和end双指针分别指向滑动窗口的左右两端
class Solution3:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = n + 1
        count = 0
        start, end = 0, 0
        while end < n:
            count += nums[end]
            while count >= target:
                res = min(res, end - start + 1)
                count -= nums[start]
                start += 1
            end += 1
        return res if res != n + 1 else 0


if __name__ == '__main__':
    target1 = 7
    nums1 = [2, 3, 1, 2, 4, 3]
    target2 = 4
    nums2 = [1, 4, 4]
    target3 = 11
    nums3 = [1, 1, 1, 1, 1, 1, 1, 1]
    s1 = Solution1()
    s2 = Solution2()
    s3 = Solution3()
    print(s1.minSubArrayLen(target1, nums1))
    print(s1.minSubArrayLen(target2, nums2))
    print(s1.minSubArrayLen(target3, nums3))
    print(s2.minSubArrayLen(target1, nums1))
    print(s2.minSubArrayLen(target2, nums2))
    print(s2.minSubArrayLen(target3, nums3))
    print(s3.minSubArrayLen(target1, nums1))
    print(s3.minSubArrayLen(target2, nums2))
    print(s3.minSubArrayLen(target3, nums3))
    map()
