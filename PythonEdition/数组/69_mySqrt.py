# 方法1-二分法
class Solution1:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0
        while l <= r:
            mid = l + (r - l) // 2
            if mid ** 2 <= x:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res

# 方法2-牛顿迭代法
class Solution2:
    def mySqrt(self, x: int) -> int:
        pass


if __name__ == '__main__':
    x1 = 4
    x2 = 8
    s1 = Solution1()
    # s2 = Solution2()
    print(s1.mySqrt(x1))
    print(s1.mySqrt(x2))
    # print(s2.mySqrt(x1))
    # print(s2.mySqrt(x2))