from typing import List


# 方法1-按螺旋模拟
class Solution1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dire_idx = 0
        row = col = 0
        res = []
        for i in range(m * n):
            res.append(matrix[row][col])
            visited[row][col] = True
            dx, dy = directions[dire_idx]
            next_row, next_col = row + dx, col + dy
            if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n or visited[next_row][next_col] is True:
                dire_idx = (dire_idx + 1) % 4
                dx, dy = directions[dire_idx]
            row, col = row + dx, col + dy
        return res


# 方法2-按层模拟
class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, m - 1, 0, n - 1
        res = []
        count = m * n
        while count >= 1:
            for col in range(left, right + 1):
                if count >= 1:  # 如果是正方形则无需加上这句话，长方形则必须要加入
                    res.append(matrix[top][col])
                    count -= 1
            top += 1
            for row in range(top, bottom + 1):
                if count >= 1:
                    res.append(matrix[row][right])
                    count -= 1
            right -= 1
            for col in range(right, left - 1, -1):
                if count >= 1:
                    res.append(matrix[bottom][col])
                    count -= 1
            bottom -= 1
            for row in range(bottom, top - 1, -1):
                if count >= 1:
                    res.append(matrix[row][left])
                    count -= 1
            left += 1
        return res


if __name__ == '__main__':
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    s1 = Solution1()
    s2 = Solution2()
    print(s1.spiralOrder(matrix1))
    print(s1.spiralOrder(matrix2))
    print(s2.spiralOrder(matrix1))
    print(s2.spiralOrder(matrix2))