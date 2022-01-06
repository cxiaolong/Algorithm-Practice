from typing import List


# 深度优先搜索
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, r, c):
            grid[r][c] = "0"  # 将搜索过的位置值设为0，防止死循环
            for x, y in [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= x < row and 0 <= y < col and grid[x][y] == "1":
                    dfs(grid, x, y)

        land_nums = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    land_nums += 1
        return land_nums


class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dps(grid, x, y):
            grid[x][y] = "0"  # 将搜索过的节点置为0，防止重复搜索
            for dx, dy in directions:
                newx = x+dx
                newy = x+dy
                if 0 <= newx < row and 0 <= newy < col and grid[newy][newx] == "1":
                    dps(grid, newx, newy)
        row = len(grid)
        col = len(grid[0])
        land_nums = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    land_nums += 1
                    dps(grid, i, j)
        return land_nums


if __name__ == '__main__':
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    s = Solution()
    print(s.numIslands(grid1))
    print(s.numIslands(grid2))
