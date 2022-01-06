from typing import List


# 方法1-
class Solution1:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 先按照身高从高到低排序，确定第一个维度
        # 当身高h相同时，按照第二个维度k排序
        people.sort(key=lambda x: (-x[0], x[1]))
        que = []
        # 然后按照k进行插入
        for p in people:
            que.insert(p[1], p)
        return que



if __name__ == '__main__':
    people1 = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    people2 = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
    s1 = Solution1()
    print(s1.reconstructQueue(people1))
    print(s1.reconstructQueue(people2))