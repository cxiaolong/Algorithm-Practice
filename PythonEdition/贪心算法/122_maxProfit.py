from typing import List

# 方法1-贪心算法
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                res += (prices[i+1] - prices[i])
                i += 1
        return res


# 方法二-动态规划
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        pass



if __name__ == '__main__':
    prices1 = [7, 1, 5, 3, 6, 4]
    prices2 = [1, 2, 3, 4, 5]
    prices3 = [7, 6, 4, 3, 1]
    s1 = Solution1()
    s2 = Solution2()
    print(s1.maxProfit(prices1))
    print(s1.maxProfit(prices2))
    print(s1.maxProfit(prices3))