from typing import List


# 方法1-深度优先搜索+回溯算法
class Solution1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 回溯算法都可以抽象为树形结构
        # 回溯算法解决的是在集合中递归查找子集，集合的大小构成了树的宽度，递归的深度构成了树的深度
        # 回溯递归的终止条件是遍历到叶子节点
        # for循环用于横向遍历，backtrack用于纵向遍历
        def dfs(n, k, start_index, path):
            """
            n相当于树的高度，k相当于树的宽度
            :param n: 给定的上限值
            :param k: 给定的组合的大小
            :param start_index: 最开始搜索的节点
            :param path: 当前的搜索路径
            """
            if len(path) == k:
                res.append(path.copy())
                return
            # start_index:每次从集合中选取元素，可选择的范围随着选择的进行而收缩，调整可选择的范围
            for i in range(start_index, n + 1):
                path.append(i)
                dfs(n, k, i + 1, path)
                path.pop()

        res = []
        dfs(n, k, 1, [])
        return res


# 方法2-剪枝优化
class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 剪枝的地方就在递归中每一层for循环所选择的起始位置
        # 当for循环起始位置之后的元素已经不足，我们就没必要继续搜索了
        def track_back(n, k, start_index, path):
            if len(path) == k:
                res.append(path.copy())
                return
            for i in range(start_index, n - (k - len(path)) + 2):
                path.append(i)
                track_back(n, k, i + 1, path)
                path.pop()

        res = []
        track_back(n, k, 1, [])
        return res


if __name__ == '__main__':
    s1 = Solution1()
    s2 = Solution2()
    print(s1.combine(4, 2))
    print(s2.combine(4, 2))
