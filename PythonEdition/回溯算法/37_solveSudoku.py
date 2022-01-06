from typing import List


# 方法1-递归
class Solution1:
    def solveSudoku(self, board: List[List[str]]) -> None:
        pass


# 方法2-位运算优化
class Solution2:
    def solveSudoku(self, board: List[List[str]]) -> None:
        pass


# 方法3-枚举优化
class Solution3:
    def solveSudoku(self, board: List[List[str]]) -> None:
        pass


# 方法4-回溯算法
class Solution4:
    def solveSudoku(self, board: List[List[str]]) -> None:
        pass


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    s1 = Solution1()
    s4 = Solution4()
    print(s4.solveSudoku(board))
