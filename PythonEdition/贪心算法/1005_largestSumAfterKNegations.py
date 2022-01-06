from typing import List


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A = sorted(A, key=abs, reverse=True)  # 将A按照绝对值从大到小排序
        for i in range(len(A)):
            if K > 0 and (A[i] < 0):
                A[i] *= -1
                K -= 1
        if K > 0:
            A[-1] *= (-1) ** K
        return sum(A)


if __name__ == '__main__':
    A1 = [4, 2, 3]
    K1 = 1
    A2 = [3, -1, 0, 2]
    K2 = 3
    A3 = [2, -3, -1, 5, -4]
    K3 = 2
    s = Solution()
    print(s.largestSumAfterKNegations(A1, K1))
    print(s.largestSumAfterKNegations(A2, K2))
    print(s.largestSumAfterKNegations(A3, K3))
