from collections import Counter, defaultdict
from typing import List


# 方法1
class Solution1:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            if i in nums2:
                res.append(i)
                nums2.remove(i)
        return res


# 方法2-计数（Counter）
class Solution2:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        res = []
        cnt_nums1 = Counter(nums1)
        for num in nums2:
            if cnt_nums1.get(num, 0) > 0:
                res.append(num)
                cnt_nums1[num] -= 1

        return res


# 方法3-计数（defaultdict）
class Solution3:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        res = []
        count = defaultdict(int)
        for i in nums1:
            count[i] += 1
        for j in nums2:
            if count[j] > 0:
                res.append(j)
                count[j] -= 1
        return res
        

# 方法4-排序+双指针
class Solution4:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        m, n = len(nums1), len(nums2)
        index1, index2 = 0, 0
        res = []
        while index1 < m and index2 < n:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                res.append(nums1[index1])
                index1 += 1
                index2 += 1
        return res


if __name__ == '__main__':
    nums11 = [1, 2, 2, 1]
    nums12 = [2, 2]
    nums21 = [4, 9, 5]
    nums22 = [9, 4, 9, 8, 4]
    so1 = Solution1()
    so2 = Solution2()
    so3 = Solution3()
    so4 = Solution4()
    # print(so1.intersect(nums11, nums12))
    # print(so1.intersect(nums21, nums22))
    # print(so2.intersect(nums11, nums12))
    # print(so2.intersect(nums21, nums22))
    # print(so3.intersect(nums11, nums12))
    # print(so3.intersect(nums21, nums22))
    print(so4.intersect(nums11, nums12))
    print(so4.intersect(nums21, nums22))