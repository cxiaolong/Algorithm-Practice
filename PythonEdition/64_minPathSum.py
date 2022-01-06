from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        dp[0][0] = grid[0][0]
        # 第一行
        for i in range(1, col):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        # 第一列
        for i in range(1, row):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    grid2 = [[1, 2, 3], [4, 5, 6]]
    print(s.minPathSum(grid))
    print(s.minPathSum(grid2))
