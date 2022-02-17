from collections import defaultdict


class Solution1:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ""
        i = 0
        res = (0, m + 1)
        need = defaultdict(int)
        for c in t:
            need[c] += 1
        need_count = n
        for j, c in enumerate(s):
            if need[c] > 0:
                need_count -= 1
            need[c] -= 1
            if need_count == 0:  # 当滑窗包含了t中所有字符时
                while True:
                    if need[s[i]] == 0:  # 恰好该窗口包含所有字符
                        break
                    need[s[i]] += 1
                    i += 1  # 左指针移动，缩小窗口
                if j - i < res[1] - res[0]:
                    res = (i, j)

                need[s[i]] += 1
                need_count += 1
                i += 1  # 左指针右移，寻找下一结果

        return "" if res[1] - res[0] == m + 1 else s[res[0]:res[1] + 1]


if __name__ == '__main__':
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    s2 = "a"
    t2 = "a"
    s3 = "a"
    t3 = "aa"
    so1 = Solution1()
    print(so1.minWindow(s1, t1))
    print(so1.minWindow(s2, t2))
    print(so1.minWindow(s3, t3))
