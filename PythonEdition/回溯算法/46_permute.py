import itertools
from typing import List


# 方法1-利用python现有的排列库（开挂操作）
class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))


# 方法2-深度优先搜索+回溯算法：状态变量：搜索深度depth、搜索路径path、记录数字是否被选取的布尔数组is_used
class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 构建深度优先搜索的函数
        def dfs(nums, size, depth, path, is_used, res):
            """
            :param nums: 原始数组
            :param size: 原始数组大小
            :param depth: 当前搜索深度
            :param path: 当前的搜索路径
            :param is_used: 数组中元素是否已经被使用
            :param res: 保存数字全排列的动态数组
            """
            if depth == size:  # 当搜索深度等于原始数组大小时，已经搜索到叶子节点，搜索结束，将完整的搜索结果添加到排列数组，退出
                res.append(path.copy())   # 这里要拷贝一份path，path所指向的列表在深度优先遍历的过程中只有一份，最后回溯到根节点，path变为空
                return
            # 依次选择未被选择的数，作为下一个深度的元素
            for i in range(size):
                if is_used[i] is False:
                    path.append(nums[i])
                    is_used[i] = True

                    dfs(nums, size, depth + 1, path, is_used, res)  # 继续向下所搜，这是一个递归操作，参数depth更新为depth+1

                    # 回溯操作，回溯到上一层的状态
                    is_used[i] = False
                    path.pop()
        res = []
        size = len(nums)
        if size != 0:
            is_used = [False for _ in range(size)]
            dfs(nums, size, 0, [], is_used, res)
        return res


# 方法3-回溯算法+动态维护数组
class Solution3:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            if first == n:
                res.append(nums.copy())
                return
            # 遍历的过程中动态维护这个数组，遍历过程中会将使用过的元素放到first当前位置
            # first之前的数表示已经使用，first之后的数表示未被使用的
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)  # 递归
                nums[first], nums[i] = nums[i], nums[first]  # 再次回到原来的状态

        n = len(nums)
        res = []
        backtrack()
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    s1 = Solution1()
    s2 = Solution2()
    s3 = Solution3()
    print(s1.permute(nums))
    print(s2.permute(nums))
    print(s3.permute(nums))
