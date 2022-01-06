from typing import List


# 方法1-模拟
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        columns = len(matrix[0])
        size = rows * columns

        order = [0] * size
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        is_visited = [[False] * columns for _ in range(rows)]

        direction_index = 0
        row, col = 0, 0  # 初始位置
        for i in range(size):
            order[i] = matrix[row][col]
            is_visited[row][col] = True
            next_row, next_col = row + direction[direction_index][0], col + direction[direction_index][1]
            if not (0 <= next_row < rows and 0 <= next_col < columns and not is_visited[next_row][next_col]):
                direction_index = (direction_index + 1) % 4
            row += direction[direction_index][0]
            col += direction[direction_index][1]
        return order


if __name__ == '__main__':
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    s1 = Solution()
    print(s1.spiralOrder(matrix1))
    print(s1.spiralOrder(matrix2))
