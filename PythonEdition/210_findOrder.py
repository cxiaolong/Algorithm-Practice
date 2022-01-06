from typing import List


# 广度优先搜索
class Solution:
    def canOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 存储有向图
        edges = {}
        # 存储每个节点的入度
        indeg = [0] * numCourses
        # 存储答案
        result = []

        for info in prerequisites:
            edges[info[1]] = info[0]
            indeg[info[0]] += 1

        # 将所有入度为0的节点放入队列中
        queue = [i for i in range(numCourses) if indeg[i] == 0]
        print(queue)

        while queue:
            # 从队列中取出一个节点
            u = queue.pop(0)
            # 放入答案中
            result.append(u)
            for k, v in edges.items():
                if k == u:
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        queue.append(v)
        if len(result) == numCourses:
            return result


if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

    s = Solution()
    print(s.canOrder(numCourses, prerequisites))
