# 方法1-字符字典
class Solution1:
    def replaceSpace(self, s: str) -> str:
        res = []
        for c in s:
            if c != " ":
                res.append(c)
            else:
                res.append("%20")

        return "".join(res)


# 方法2-replace函数
class Solution2:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ", "%20")


# 方法3-双指针替换
class Solution3:
    def replaceSpace(self, s: str) -> str:
        # 新字符串的长度是比原字符串长"空格数 * 2"
        new_s = list(s) + [" "] * s.count(" ") * 2

        # 两个指针分别指向字符串的末尾
        cur1, cur2 = len(s) - 1, len(new_s) - 1
        while cur1 != cur2:  # 当两个指针大小相等时，则说明字符串前面没有空格了
            if new_s[cur1] != " ":
                new_s[cur2] = s[cur1]
                cur2 -= 1  # cur2向前走一步
            else:
                new_s[cur2 - 2: cur2 + 1] = "%20"
                cur2 -= 3  # cur2向前走3步
            cur1 -= 1
        return "".join(new_s)


if __name__ == '__main__':
    s = "We are happy."
    so1 = Solution1()
    so2 = Solution2()
    so3 = Solution3()
    print(so1.replaceSpace(s))
    print(so2.replaceSpace(s))
    print(so3.replaceSpace(s))
