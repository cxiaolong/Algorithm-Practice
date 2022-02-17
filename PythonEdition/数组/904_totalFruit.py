from collections import Counter
from typing import List


# 方法1-滑动窗口：利用Python集合去重（超时）
class Solution1:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        res = 0
        start = end = 0
        while end < n:
            end += 1
            if len(set(fruits[start:end])) <= 2:  # 利用set去重，判断窗口内的水果种类是否大于2
                res = max(res, end - start)
            else:
                start += 1  # 当窗口内水果种类大于2时，左指针移动，收缩窗口
        return res


# 方法2-滑动窗口+计数器
class Solution2:
    def totalFruit(self, fruits: List[int]) -> int:
        res = idx = 0
        count = Counter()
        for i, x in enumerate(fruits):
            count[x] += 1
            while len(count) >= 3:  # 当计数器中有三个及以上值时，需要移动前指针收缩窗口
                count[fruits[idx]] -= 1
                if count[fruits[idx]] == 0:  # 当计数为0时，需要删除
                    del count[fruits[idx]]
                idx += 1
            res = max(res, i - idx + 1)
        return res


if __name__ == '__main__':
    fruits1 = [1, 2, 1]
    fruits2 = [0, 1, 2, 2]
    fruits3 = [1, 2, 3, 2, 2]
    fruits4 = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    s1 = Solution1()
    s2 = Solution2()
    print(s1.totalFruit(fruits1))
    print(s1.totalFruit(fruits2))
    print(s1.totalFruit(fruits3))
    print(s1.totalFruit(fruits4))
    print(s2.totalFruit(fruits1))
    print(s2.totalFruit(fruits2))
    print(s2.totalFruit(fruits3))
    print(s2.totalFruit(fruits4))