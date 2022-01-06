from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        # 初始化dp数组
        dp = [[0 for _ in range(col)] for _ in range(row)]
        dp[0][0] = 0 if obstacleGrid[0][0] == 1 else 1
        # 如果左上角的位置就是障碍物，则直接返回
        if dp[0][0] == 0:
            return 0
        # 第一列
        for i in range(1, row):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i-1][0]
        # 第一行
        for j in range(1, col):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = dp[0][j-1]

        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsWithObstacles(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
