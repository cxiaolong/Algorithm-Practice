from typing import List


# 方法1-回溯算法
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates, target, path, start_index):
            if sum(path) == target:
                res.append(path.copy())
                return
            elif sum(path) > target:
                return
            for i in range(start_index, len(candidates)):
                path.append(candidates[i])
                backtrack(candidates, target, path, i)
                path.pop()

        res = []
        if len(candidates) != 0:
            backtrack(candidates, target, [], 0)
        return res


# 方法2-回溯算法2
class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(nums, target, path, start, res):
            if target == 0:
                res.append(path.copy())
                return
            if target < 0:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(nums, target - nums[i], path, i, res)  # 这一步start从i开始
                path.pop()
                i += 1

        res = []
        if len(candidates) != 0:
            backtrack(candidates, target, [], 0, res)
        return res


# 方法3-剪枝优化
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates, target, path, start_index):
            if sum(path) == target:
                res.append(path.copy())
                return
            elif sum(path) > target:
                return
            for i in range(start_index, len(candidates)):
                if sum(path) + candidates[i] > target:
                    return
                path.append(candidates[i])
                backtrack(candidates, target, path, i)
                path.pop()

        res = []
        if len(candidates) != 0:
            candidates.sort()
            backtrack(candidates, target, [], 0)
        return res


if __name__ == '__main__':
    s = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    candidates2 = [2, 3, 5]
    target2 = 8
    print(s.combinationSum(candidates, target))
    print(s.combinationSum(candidates2, target2))
