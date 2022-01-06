import itertools
from typing import List


# 方法1-利用python库函数
class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)+1):
            for temp in itertools.combinations(nums, i):
                res.append(list(temp))

        return res


# 方法2-迭代
class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]

# 方法3-回溯算法
class Solution3:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path, start_index):
            res.append(path.copy())  # 将所有搜索到均添加
            for i in range(start_index, len(nums)):
                path.append(nums[i])
                backtrack(nums, path, i + 1)
                path.pop()
        res = []
        backtrack(nums, [], 0)
        return res




if __name__ == '__main__':
    nums = [1, 2, 3]
    s1 = Solution1()
    s3 = Solution3()
    print(s1.subsets(nums))
    print(s3.subsets(nums))