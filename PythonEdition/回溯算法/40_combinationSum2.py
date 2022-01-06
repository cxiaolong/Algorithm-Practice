from typing import List


# 此解法超出时间限制
class Solution1:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates, target, path, start_index):
            if sum(path) == target:
                if path not in res:
                    res.append(path.copy())
                return
            elif sum(path) > target:
                return
            for i in range(start_index, len(candidates)):
                if sum(path) + candidates[i] > target:
                    return
                path.append(candidates[i])
                backtrack(candidates, target, path, i+1)
                path.pop()

        res = []
        candidates.sort()
        backtrack(candidates, target, [], 0)
        return res


# "树层去重"
class Solution2:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates, target, sum, startIndex):
            if sum == target:
                res.append(path[:])
            for i in range(startIndex, len(candidates)):  # 要对同一树层使用过的元素进行跳过
                if sum + candidates[i] > target:  # 剪枝
                    return
                if i > startIndex and candidates[i] == candidates[i - 1]:
                    continue  # 直接用startIndex来去重,要对同一树层使用过的元素进行跳过
                sum += candidates[i]
                path.append(candidates[i])
                backtrack(candidates, target, sum, i + 1)  # i+1:每个数字在每个组合中只能使用一次
                sum -= candidates[i]  # 回溯
                path.pop()  # 回溯

        res = []
        path = []
        candidates = sorted(candidates)  # 首先把给candidates排序，让其相同的元素都挨在一起。
        backtrack(candidates, target, 0, 0)
        return res


class Solution3:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates, target, path, start_index):
            if sum(path) == target:
                res.append(path.copy())
                return
            for i in range(start_index, len(candidates)):
                if sum(path) + candidates[i] > target:
                    return
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(candidates, target, path, i + 1)
                path.pop()
        res = []
        backtrack(sorted(candidates), target, [], 0)
        return res


if __name__ == '__main__':
    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    candidates2 = [2, 5, 2, 1, 2]
    target2 = 5
    s1 = Solution1()
    s2 = Solution2()
    print(s1.combinationSum2(candidates1, target1))
    print(s1.combinationSum2(candidates2, target2))
    print(s2.combinationSum2(candidates1, target1))
    print(s2.combinationSum2(candidates2, target2))
