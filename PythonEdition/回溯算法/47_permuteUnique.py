from typing import List


# 方法1-深度优先搜索+回溯算法
class Solution1:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, is_used, res):
            if depth == size:
                if path not in res:
                    res.append(path.copy())
                    return

            for i in range(size):
                if is_used[i] is False:
                    path.append(nums[i])
                    is_used[i] = True
                    dfs(nums, size, depth + 1, path, is_used, res)
                    path.pop()
                    is_used[i] = False

        res = []
        size = len(nums)
        if size != 0:
            is_used = [False for _ in range(size)]
            dfs(nums, size, 0, [], is_used, res)
        return res


# 方法2-边搜索边去重（效率更高）
class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, n, path, used):
            if len(path) == n:
                res.append(path.copy())
                return
            for i in range(n):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i-1]:
                        continue
                    path.append(nums[i])
                    used[i] = True
                    backtrack(nums, n, path, used)
                    path.pop()
                    used[i] = False
        res = []
        n = len(nums)
        used = [False] * n
        backtrack(sorted(nums), n, [], used)
        return res


if __name__ == '__main__':
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    s1 = Solution1()
    s2 = Solution2()
    print(s1.permuteUnique(nums1))
    print(s1.permuteUnique(nums2))
    print(s2.permuteUnique(nums1))
    print(s2.permuteUnique(nums2))
