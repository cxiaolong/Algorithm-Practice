from collections import Counter
from typing import List


# 方法1- LeetCode执行 6652 ms
class Solution1:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        n, m = len(s), len(p)
        if n >= m:
            count = Counter(p)
            for i in range(n - m + 1):
                sub_str = s[i:i + m]
                if count == Counter(sub_str):
                    res.append(i)
        return res


# 方法2-改进为滑动窗口+数组
class Solution2:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m, res = len(s), len(p), []
        if n < m: return res

        count_p = [0] * 26
        count_s = [0] * 26
        for i in range(m):
            count_p[ord(p[i]) - ord('a')] += 1
            count_s[ord(s[i]) - ord('a')] += 1

        if count_p == count_s:
            res.append(0)

        for i in range(m, n):
            count_s[ord(s[i - m]) - ord('a')] -= 1
            count_s[ord(s[i]) - ord('a')] += 1
            if count_p == count_s:
                res.append(i - m + 1)

        return res


# 方法3-滑动窗口+双指针
class Solution3:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m, res = len(s), len(p), []
        if n < m: return res

        s_cnt = [0] * 26
        p_cnt = [0] * 26
        for i in p:
            p_cnt[ord(i) - ord('a')] += 1

        left = 0
        for right in range(n):
            right_index = ord(s[right]) - ord('a')
            s_cnt[right_index] += 1
            while s_cnt[right_index] > p_cnt[right_index]:
                left_index = ord(s[left]) - ord('a')
                s_cnt[left_index] -= 1
                left += 1
            if right - left + 1 == m:
                res.append(left)

        return res



if __name__ == '__main__':
    s1 = "cbaebabacd"
    p1 = "abc"
    s2 = "abab"
    p2 = "ab"
    so1 = Solution1()
    so2 = Solution2()
    so3 = Solution3()
    print(so1.findAnagrams(s1, p1))
    print(so1.findAnagrams(s2, p2))
    print(so2.findAnagrams(s1, p1))
    print(so2.findAnagrams(s2, p2))
    print(so3.findAnagrams(s1, p1))
    print(so3.findAnagrams(s2, p2))
