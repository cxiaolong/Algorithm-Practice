from typing import List


# 方法1-贪心算法
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy_list = [1] * len(ratings)
        for i in range(len(ratings) - 1):
            if ratings[i] < ratings[i+1]:
                candy_list[i+1] = candy_list[i] + 1
        for j in range(len(ratings) - 1, 0, -1):
            if ratings[j-1] > ratings[j]:
                candy_list[j-1] = max(candy_list[j-1], candy_list[j] + 1)
        return sum(candy_list)



if __name__ == '__main__':
    ratings1 = [1, 0, 2]
    ratings2 = [1, 2, 2]
    ratings3 = [1, 2, 2, 5, 4, 3, 2]
    s = Solution()
    print(s.candy(ratings1))
    print(s.candy(ratings2))
    print(s.candy(ratings3))
