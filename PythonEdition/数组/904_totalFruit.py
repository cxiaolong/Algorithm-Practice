from typing import List


class Solution1:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        res = 0
        start = end = 0
        while end < n:
            end += 1
            if len(tuple(fruits[start:end+1])) <= 2:
                res = max(res, end - start + 1)
            else:
                start += 1
                continue
        return res


if __name__ == '__main__':
    fruits1 = [1, 2, 1]
    fruits2 = [0, 1, 2, 2]
    fruits3 = [1, 2, 3, 2, 2]
    s1 = Solution1()
    print(s1.totalFruit(fruits1))
    print(s1.totalFruit(fruits2))
    print(s1.totalFruit(fruits3))