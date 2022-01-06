from typing import List


class Solution1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        pass


if __name__ == '__main__':
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    s1 = Solution1()
    print(s1.spiralOrder(matrix1))
    print(s1.spiralOrder(matrix2))