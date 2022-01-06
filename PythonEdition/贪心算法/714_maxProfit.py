from typing import List


# 方法1-贪心算法
class Solution1:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        min_price = prices[0] + fee
        profit = 0
        for price in prices:
            if price + fee < min_price:
                min_price = price + fee
            elif price > min_price:
                profit += price - min_price
                min_price = price
        return profit


# 方法2-动态规划
class Solution2:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        pass


if __name__ == '__main__':
    prices1 = [1, 3, 2, 8, 4, 9]
    fee1 = 2
    prices2 = [1, 3, 7, 5, 10, 3]
    fee2 = 3
    s1 = Solution1()
    s2 = Solution2()
    print(s1.maxProfit(prices1, fee1))
    print(s1.maxProfit(prices2, fee2))
    print(s2.maxProfit(prices1, fee1))
    print(s2.maxProfit(prices2, fee2))
