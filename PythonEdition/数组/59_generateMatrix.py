from typing import List


# 方法1-按螺旋模拟
class Solution1:
    """
    time complexity: O(n*n)
    space complexity: O(1)
    """

    def generateMatrix(self, n: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        matrix = [[0] * n for _ in range(n)]
        row, col = 0, 0
        dir_idx = 0
        for i in range(n * n):
            matrix[row][col] = i + 1
            dx, dy = directions[dir_idx]
            next_row, next_col = row + dx, col + dy
            if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n or matrix[next_row][next_col] > 0:
                dir_idx = (dir_idx + 1) % 4
                dx, dy = directions[dir_idx]
            row, col = row + dx, col + dy
        return matrix


# 方法2-按层模拟
class Solution2:
    """
    time complexity: O(n*n)
    space complexity: O(1)
    """

    def generateMatrix(self, n: int) -> List[List[int]]:
        num = 1
        left, top, right, bottom = 0, 0, n - 1, n - 1
        matrix = [[0] * n for _ in range(n)]
        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            for row in range(top + 1, bottom + 1):
                matrix[row][bottom] = num
                num += 1
            for col in range(right - 1, left, -1):
                matrix[bottom][col] = num
                num += 1
            for row in range(bottom, top, -1):
                matrix[row][left] = num
                num += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return matrix


# 方法3-按层模拟，以填充的数为终止条件
class Solution3:
    """
    time complexity: O(n*n)
    space complexity: O(1)
    """

    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right, top, bottom = 0, n - 1, 0, n - 1
        num = 1
        matrix = [[0] * n for _ in range(n)]
        while num <= n * n:
            for col in range(left, right + 1):  # left to right
                matrix[top][col] = num
                num += 1
            top += 1
            for row in range(top, bottom + 1):  # top to bottom
                matrix[row][right] = num
                num += 1
            right -= 1
            for col in range(right, left - 1, -1):  # right to left
                matrix[bottom][col] = num
                num += 1
            bottom -= 1
            for row in range(bottom, top - 1, -1):  # bottom to top
                matrix[row][left] = num
                num += 1
            left += 1
        return matrix


if __name__ == '__main__':
    n1 = 3
    n2 = 1
    s1 = Solution1()
    s2 = Solution2()
    s3 = Solution3()
    print(s1.generateMatrix(n1))
    print(s1.generateMatrix(n2))
    print(s2.generateMatrix(n1))
    print(s2.generateMatrix(n2))
    print(s3.generateMatrix(n1))
    print(s3.generateMatrix(n2))
