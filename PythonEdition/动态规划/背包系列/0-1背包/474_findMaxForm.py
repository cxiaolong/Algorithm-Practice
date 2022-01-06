from typing import List


# 方法1-将其看作01背包的扩展，背包具有2个纬度，即双层背包，不同层的背包负责装入不同的物品
class Solution1:
    # dp[i][j][k]表示最多含有j个0、k个1、索引为[0-i]的子串的最大长度
    # dp[0][j][k]
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(length + 1)]
        for i in range(1, length + 1):
            zeros = strs[i - 1].count('0')
            ones = strs[i - 1].count('1')
            for j in range(0, m + 1):
                for k in range(0, n + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if zeros <= j and ones <= k:
                        dp[i][j][k] = max(dp[i - 1][j - zeros][k - ones] + 1, dp[i][j][k])
        return dp[length][m][n]


# 方法2-空间优化：滚动数组
class Solution2:
    # 由于dp[i][][]的计算只与dp[i-1][][]有关，因此，可以可以利用滚动数组的方法去掉dp的第一个纬度
    # dp[i][j]表示最多有i个"0"和j个"1"的最大子集的大小为dp[i][j]
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for str in strs:
            zeros = str.count("0")
            ones = str.count("1")
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[m][n]


if __name__ == '__main__':
    strs1 = ["10", "0001", "111001", "1", "0"]
    m1 = 5
    n1 = 3
    strs2 = ["10", "0", "1"]
    m2 = 1
    n2 = 1
    s1 = Solution1()
    s2 = Solution2()
    print(s1.findMaxForm(strs1, m1, n1))
    print(s1.findMaxForm(strs2, m2, n2))
    print(s2.findMaxForm(strs1, m1, n1))
    print(s2.findMaxForm(strs2, m2, n2))
