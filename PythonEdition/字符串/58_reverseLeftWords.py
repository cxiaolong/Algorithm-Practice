class Solution1:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s_split = list(s)
        m = len(s)
        res = s_split[n: m]
        res.extend(s_split[0: n])
        return "".join(res)


class Solution2:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


if __name__ == '__main__':
    s1 = "abcdefg"
    k1 = 2
    s2 = "lrloseumgh"
    k2 = 6
    so1 = Solution1()
    so2 = Solution2()
    print(so1.reverseLeftWords(s1, k1))
    print(so1.reverseLeftWords(s2, k2))
    print(so2.reverseLeftWords(s1, k1))
    print(so2.reverseLeftWords(s2, k2))