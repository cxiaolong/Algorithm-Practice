from typing import List


# 方法1-搜索完去重耗时长，容易超时
class Solution1:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path, start_index):
            if len(path) >= 2 and path not in res:
                res.append(path.copy())
            for i in range(start_index, len(nums)):
                if not path or (path[-1] <= nums[i]):
                    path.append(nums[i])
                    backtrack(nums, path, i + 1)
                    path.pop()

        res = []
        backtrack(nums, [], 0)
        return res


# 方法2-边搜索边去重
class Solution2:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path, start_index):
            used = []  # 用于记录该层中使用过的数字
            if len(path) >= 2:
                res.append(path.copy())
            for i in range(start_index, len(nums)):
                if nums[i] not in used:
                    if not path or path[-1] <= nums[i]:
                        used.append(nums[i])
                        path.append(nums[i])
                        backtrack(nums, path, i + 1)
                        path.pop()
        res = []
        backtrack(nums, [], 0)
        return res


if __name__ == '__main__':
    nums1 = [4, 6, 7, 7]
    nums2 = [4, 4, 3, 2, 1]
    s1 = Solution1()
    s2 = Solution2()
    print(s1.findSubsequences(nums1))
    print(s1.findSubsequences(nums2))
    print(s2.findSubsequences(nums1))
    print(s2.findSubsequences(nums2))
