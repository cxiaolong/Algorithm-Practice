# 方法1-二分法
class Solution1:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l <= r:
            mid = l + (r - l) // 2
            if mid ** 2 < num:
                l = mid + 1
            elif mid ** 2 > num:
                r = mid - 1
            else:
                return True
        return False


# 方法2-牛顿迭代法
class Solution2:
    def isPerfectSquare(self, num: int) -> bool:
        pass


if __name__ == '__main__':
    num1 = 16
    num2 = 14
    s1 = Solution1()
    print(s1.isPerfectSquare(num1))
    print(s1.isPerfectSquare(num2))
