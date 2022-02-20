class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # 从2k的倍数开始反转k个长度的字串
        t = list(s)
        for i in range(0, len(t), 2 * k):
            t[i: i + k] = reversed(t[i: i + k])
        return "".join(t)


if __name__ == '__main__':
    so = Solution()
    s1 = "abcdefg"
    k1 = 2
    s2 = "abcd"
    k2 = 2
    print(so.reverseStr(s1, k1))
    print(so.reverseStr(s2, k2))