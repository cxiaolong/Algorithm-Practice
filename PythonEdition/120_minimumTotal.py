from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        size = len(triangle)
        if size == 0:
            return 0
        dp = [[0] * (i+1) for i in range(size)]
        dp[0][0] = triangle[0][0]
        for i in range(1, size):
            dp[i][0] = dp[i-1][0]+triangle[i][0]
            for j in range(1, i):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]

        return min(dp[-1])


if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    triangle2 = [[-10]]
    s = Solution()
    print(s.minimumTotal(triangle))
    print(s.minimumTotal(triangle2))