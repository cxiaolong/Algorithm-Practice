from functools import reduce
from typing import List


# 位运算：a ^ 0 = a, a ^ a = 0, 再利用结合律和交换律
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)






if __name__ == '__main__':
    s1 = Solution1()