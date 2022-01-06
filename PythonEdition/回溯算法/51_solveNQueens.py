from typing import List


# 方法1-基于集合的回溯
class Solution1:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_valid(row, col, columns, diagonal1, diagonal2):
            if col in columns:  # 判断同一列是否冲突
                return False
            if col - row in diagonal1:  # 判断左上角是否冲突
                return False
            if col + row in diagonal2:  # 判断右上角是否冲突
                return False
            return True

        def backtrack(n, row, columns, diagonal1, diagonal2):
            if row == n:
                solutions.append(board)
            for i in range(n):
                if is_valid(row, i, columns, diagonal1, diagonal2):
                    board[row][i] = "Q"
                    columns.append(i)
                    diagonal1.append(i - row)
                    diagonal2.append(i + row)
                    backtrack(n, row + 1, columns, diagonal1, diagonal2)
                    columns.pop()
                    diagonal1.pop()
                    diagonal2.pop()

        solutions = list()
        board = [["."] * n for _ in range(n)]
        backtrack(n, 0, [], [], [])
        return solutions


# 方法2-基于位运算的回溯
class Solution2:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # TODO
        pass



if __name__ == '__main__':
    n1 = 4
    n2 = 1
    s1 = Solution1()
    s2 = Solution2()
    print(s1.solveNQueens(n1))
    print(s1.solveNQueens(n2))
