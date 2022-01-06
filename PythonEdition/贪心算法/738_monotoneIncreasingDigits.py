# 方法1-
class Solution1:
    def monotoneIncreasingDigits(self, n: int) -> int:
        a = list(str(n))
        for i in range(len(a)-1, 0, -1):
            if int(a[i]) < int(a[i-1]):
                a[i-1] = str(int(a[i-1]) - 1)
                a[i:] = '9' * (len(a) - i)
        return int("".join(a))


if __name__ == '__main__':
    N1 = 10
    N2 = 1234
    N3 = 332
    s1 = Solution1()
    print(s1.monotoneIncreasingDigits(N1))
    print(s1.monotoneIncreasingDigits(N2))
    print(s1.monotoneIncreasingDigits(N3))
