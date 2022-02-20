from typing import List

# 方法1-调用函数
class Solution1:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


# 方法2-不调用函数（自行实现）
class Solution2:
    """
    1.第一步先去除多余空格
    2.第二步将整个字符串翻转
    3.将每个单词翻转
    """
    def trim_extra_spaces(self, s: str) -> List[str]:
        left, right = 0, len(s) - 1
        # 去除字符串开头的空白符
        while s[left] == " ": left += 1
        # 去掉字符串尾部的空白符
        while s[right] == " ": right -= 1
        # 去掉中间多余的空白符
        l = []
        while left <= right:
            if s[left] != " ":
                l.append(s[left])
            elif l[-1] != " ":
                l.append(s[left])
            left += 1
        return l

    def reverse_string(self, l: List[str], left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

    def reverse_each_word(self, l: List[str]) -> None:
        n = len(l)
        start = end = 0
        while start < n:
            while end < n and l[end] != " ":
                end += 1
            # 翻转单词
            self.reverse_string(l, left=start, right=end - 1)
            start = end + 1
            end += 1

    def reverseWords(self, s: str) -> str:
        l = self.trim_extra_spaces(s)
        self.reverse_string(l, left=0, right=len(l) - 1)
        self.reverse_each_word(l)
        return "".join(l)


if __name__ == '__main__':
    so1 = Solution1()
    so2 = Solution2()
    s1 = "the sky is blue"
    s2 = "  hello world  "
    s3 = "a good   example"
    s4 = "  Bob    Loves  Alice   "
    s5 = "Alice does not even like bob"
    print(so1.reverseWords(s1))
    print(so1.reverseWords(s2))
    print(so1.reverseWords(s3))
    print(so1.reverseWords(s4))
    print(so1.reverseWords(s5))
    print(so2.reverseWords(s1))
    print(so2.reverseWords(s2))
    print(so2.reverseWords(s3))
    print(so2.reverseWords(s4))
    print(so2.reverseWords(s5))