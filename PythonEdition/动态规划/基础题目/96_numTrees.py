# 动态规划
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        # dp[i]表示当n=i时，二叉搜索树的个数
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[-1]


if __name__ == '__main__':
    n1 = 1
    n2 = 3
    s = Solution()
    print(s.numTrees(n1))
    print(s.numTrees(n2))
