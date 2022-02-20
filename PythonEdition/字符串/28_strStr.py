from typing import List


class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if m == 0: return 0
        if m < n: return -1

        for i in range(0, m - n + 1):
            if haystack[i: i + n] == needle:
                return i
        return -1


# 方法2-KMP（版本1-前缀表左移）
class Solution2:
    def get_prefix(self, n: int, s: str) -> List[int]:
        j = -1  # 初始化前缀的位置，这里是左移一步的实现
        next = [-1] * n  # 初始化前缀表
        for i in range(1, n):
            while j > -1 and s[i] != s[j + 1]:  # 当前缀不等于后缀时，回退
                j = next[j]
            if s[i] == s[j + 1]:  # 当前缀等于后缀时，继续匹配
                j += 1
            next[i] = j  # 将j（前缀的长度）赋值给next[i]
        return next

    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if n == 0: return 0
        if m < n: return -1

        next = self.get_prefix(n, needle)
        j = -1
        for i in range(m):
            while j > -1 and haystack[i] != needle[j + 1]:  # 不匹配时根据前缀表找到之前匹配过的位置
                j = next[j]
            if haystack[i] == needle[j + 1]:  # 继续向右匹配
                j += 1
            if j == n - 1:
                return i - n + 1
        return -1


# 方法3-KMP（版本2-直接使用前缀表）
class Solution3:
    def get_prefix(self, n: int, s: str) -> List[int]:
        j = 0  # 初始化前缀的位置
        next = [0] * n  # 初始化前缀表
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:  # 当前缀不等于后缀时，回退到上一步记录的位置
                j = next[j - 1]
            if s[i] == s[j]:  # 当前缀等于后缀时，继续匹配
                j += 1
            next[i] = j  # 将j（前缀的长度）赋值给next[i]
        return next

    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if n == 0: return 0
        if m < n: return -1

        next = self.get_prefix(n, needle)
        j = 0
        for i in range(m):
            while j > 0 and haystack[i] != needle[j]:  # 不匹配时根据前缀表找到之前匹配过的位置
                j = next[j - 1]
            if haystack[i] == needle[j]:  # 继续向右匹配
                j += 1
            if j == n - 1:
                return i - n + 1
        return -1


if __name__ == '__main__':
    haystack1 = "hello"
    needle1 = "ll"
    haystack2 = "aaaaa"
    needle2 = "bba"
    haystack3 = ""
    needle3 = ""
    s1 = Solution1()
    s2 = Solution2()
    s3 = Solution3()
    print(s1.strStr(haystack1, needle1))
    print(s1.strStr(haystack2, needle2))
    print(s1.strStr(haystack3, needle3))
    print(s2.strStr(haystack1, needle1))
    print(s2.strStr(haystack2, needle2))
    print(s2.strStr(haystack3, needle3))
    print(s3.strStr(haystack1, needle1))
    print(s3.strStr(haystack2, needle2))
    print(s3.strStr(haystack3, needle3))