from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def check(i: int, j: int, k: int) -> bool:
            """判断从网格的(i, j)位置出发能否搜索到单词word[k:]"""
            directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break
            visited.remove((i, j))
            return result

        row = len(board)
        col = len(board[0])
        visited = set()
        for i in range(row):
            for j in range(col):
                if check(i, j, 0):
                    return True
        return False


class Solution2:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break

            visited.remove((i, j))
            return result

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True

        return False


if __name__ == '__main__':
    board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word1 = "ABCCED"

    board2 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word2 = "SEE"

    board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word3 = "ABCB"

    s = Solution()
    s1 = Solution()
    print(s.exist(board1, word1))
    print(s.exist(board2, word2))
    print(s.exist(board3, word3))
    print(s1.exist(board3, word3))
