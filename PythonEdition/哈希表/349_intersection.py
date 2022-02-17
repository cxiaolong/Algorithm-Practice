from typing import List


class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for item in nums1:
            if item in nums2 and item not in res:
                res.append(item)
        return res


class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    nums11 = [1, 2, 2, 1]
    nums12 = [2, 2]
    nums21 = [4, 9, 5]
    nums22 = [9, 4, 9, 8, 4]
    s1 = Solution1()
    s2 = Solution2()
    print(s1.intersection(nums11, nums12))
    print(s1.intersection(nums21, nums22))
    print(s2.intersection(nums11, nums12))
    print(s2.intersection(nums21, nums22))