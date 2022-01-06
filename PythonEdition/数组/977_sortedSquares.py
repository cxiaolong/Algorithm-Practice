from typing import List


# 方法1-不讲武德（调用排序包）
class Solution1:
    """
    time complexity: O(nlogn)
    space complexity: O(logn)
    """

    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums_squared = [i ** 2 for i in nums]
        nums_sorted = sorted(nums_squared)
        return nums_sorted


# 方法2-双指针
class Solution2:
    """
    方法1没有考虑"数组nums已经按照升序排列这个条件"
    设neg为数组中负数与非负数的分界点，两个指针分别指向neg和neg+1，则可以得到2个有序的子数组
    利用归并排序对两个数组排序
    time complexity: O(n)
    space complexity: O(1)
    """

    def sortedSquares(self, nums: List[int]) -> List[int]:
        negative = -1
        n = len(nums)
        for index, value in enumerate(nums):
            if value < 0:
                negative = index
            else:
                break

        res = []
        i, j = negative, negative + 1
        while i >= 0 or j < n:
            if i < 0:
                res.append(nums[j] ** 2)
                j += 1
            elif j == n:
                res.append(nums[i] ** 2)
                i -= 1
            elif nums[i] ** 2 <= nums[j] ** 2:
                res.append(nums[i] ** 2)
                i -= 1
            else:
                res.append((nums[j] ** 2))
                j += 1
        return res


# 方法3-双指针法
class Solution3:
    """
    使用两个指针分别指向0和n-1，每次比较两个指针对应的平方数，选择较大的那个逆序放入答案
    time complexity: O(n)
    space complexity: O(1)
    """

    def sortedSquares(self, nums: List[int]):
        n = len(nums)
        res = [0] * n
        i, j, pos = 0, n - 1, n - 1
        while i <= j:
            if nums[i] ** 2 >= nums[j] ** 2:
                res[pos] = nums[i] ** 2
                i += 1
            else:
                res[pos] = nums[j] ** 2
                j -= 1
            pos -= 1
        return res


if __name__ == '__main__':
    nums1 = [-4, -1, 0, 3, 10]
    nums2 = [-7, -3, 2, 3, 11]
    s1 = Solution1()
    s2 = Solution2()
    s3 = Solution3()
    print(s1.sortedSquares(nums1))
    print(s1.sortedSquares(nums2))
    print(s2.sortedSquares(nums1))
    print(s2.sortedSquares(nums2))
    print(s3.sortedSquares(nums1))
    print(s3.sortedSquares(nums2))
