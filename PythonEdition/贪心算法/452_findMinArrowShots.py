from typing import List


# 方法1-
class Solution1:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        num_arrows = 1
        for i in range(len(points) - 1):
            if points[i][1] < points[i+1][0]:
                num_arrows += 1
            else:
                points[i+1][1] = min(points[i][1], points[i+1][1])
        return num_arrows




if __name__ == '__main__':
    points1 = [[10, 16], [2, 8], [1, 6], [7, 12]]
    points2 = [[1, 2], [3, 4], [5, 6], [7, 8]]
    points3 = [[1, 2], [2, 3], [3, 4], [4, 5]]
    points4 = [[1, 2]]
    points5 = [[2, 3], [2, 3]]
    s = Solution1()
    print(s.findMinArrowShots(points1))
    print(s.findMinArrowShots(points2))
    print(s.findMinArrowShots(points3))
    print(s.findMinArrowShots(points4))
    print(s.findMinArrowShots(points5))