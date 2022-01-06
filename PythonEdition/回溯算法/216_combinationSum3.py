from typing import List


# 方法1-直接回溯算法
class Solution1:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def track_back(n, k, start_index, path):
            if len(path) == k:
                if sum(path) == n:
                    res.append(path.copy())
                return
            for i in range(start_index, 10):
                path.append(i)
                track_back(n, k, i + 1, path)
                path.pop()

        res = []
        track_back(n, k, 1, [])
        return res


# 方法2-剪枝优化
class Solution2:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def track_back(n, k, start_index, path, total):
            if total > n:  # 剪枝操作
                return
            if total == n and len(path) == k:
                res.append(path.copy())
                return
            for i in range(start_index, 10 - (k - len(path)) + 1):  # 剪枝
                path.append(i)
                total += i
                track_back(n, k, i + 1, path, total)
                path.pop()
                total -= i

        res = []
        track_back(n, k, 1, [], 0)
        return res


if __name__ == '__main__':
    k1 = 3
    n1 = 7
    k2 = 3
    n2 = 9
    s1 = Solution1()
    s2 = Solution2()
    print(s1.combinationSum3(k1, n1))
    print(s1.combinationSum3(k2, n2))
    print(s2.combinationSum3(k1, n1))
    print(s2.combinationSum3(k2, n2))
