from typing import List


# 方法1-暴力枚举法
class Solution1:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if s == s[:i] * (n // i):
                return True
        return False


# 方法2-字符串匹配
class Solution2:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s+s).find(s, 1) != len(s)


# 方法3-KMP算法
class Solution3:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def kmp(pattern: str, length: int) -> List[int]:
            next = [0] * length  # 前缀表左移一步
            for i in range(1, length):
                j = next[i - 1]
                while j != 0 and pattern[i] != pattern[j]:
                    j = next[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                next[i] = j
            return next

        n = len(s)
        next = kmp(s, n)
        return next[-1] != 0 and n % (n - next[-1]) == 0




if __name__ == '__main__':
    s1 = "abab"
    s2 = "aba"
    s3 = "abcabcabcabc"
    so1 = Solution1()
    so2 = Solution2()
    so3 = Solution3()
    print(so1.repeatedSubstringPattern(s1))
    print(so1.repeatedSubstringPattern(s2))
    print(so1.repeatedSubstringPattern(s3))
    print(so2.repeatedSubstringPattern(s1))
    print(so2.repeatedSubstringPattern(s2))
    print(so2.repeatedSubstringPattern(s3))
    print(so3.repeatedSubstringPattern(s1))
    print(so3.repeatedSubstringPattern(s2))
    print(so3.repeatedSubstringPattern(s3))