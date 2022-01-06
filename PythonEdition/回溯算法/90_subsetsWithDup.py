from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path, start_index):
            res.append(path.copy())
            for i in range(start_index, len(nums)):
                if i > start_index and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(nums, path, i + 1)
                path.pop()
        res = []
        backtrack(sorted(nums), [], 0)
        return res


if __name__ == '__main__':
    nums1 = [1, 2, 2]
    nums2 = [0]
    s = Solution()
    print(s.subsetsWithDup(nums1))
    print(s.subsetsWithDup(nums2))