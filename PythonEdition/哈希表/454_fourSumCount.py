from collections import Counter
from typing import List


class Solution1:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        countAB = Counter(u + v for u in nums1 for v in nums2)

        ans = 0
        for i in nums3:
            for j in nums4:
                if (-i - j) in countAB:
                    ans += countAB[-i - j]
        return ans


if __name__ == '__main__':
    nums11 = [1, 2]
    nums12 = [-2, -1]
    nums13 = [-1, 2]
    nums14 = [0, 2]
    nums21 = [0]
    nums22 = [0]
    nums23 = [0]
    nums24 = [0]
    s1 = Solution1()
    print(s1.fourSumCount(nums11, nums12, nums13, nums14))
    print(s1.fourSumCount(nums21, nums22, nums23, nums24))
