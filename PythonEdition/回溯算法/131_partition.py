from typing import List


# 分割问题-回溯算法
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 如何模拟切割线
        # 如何截取字串
        # 何时递归终止
        def backtrack(s, path, start_index):
            if start_index >= len(s):
                res.append(path.copy())
            for i in range(start_index, len(s)):
                p = s[start_index:i + 1]
                if p == p[::-1]:
                    path.append(p)
                    backtrack(s, path, i + 1)
                    path.pop()
                else:
                    continue

        res = []
        backtrack(s, [], 0)
        return res


if __name__ == '__main__':
    s1 = "aab"
    s2 = "a"
    s = Solution()
    print(s.partition(s1))
    print(s.partition(s2))
