class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)
        max_length = 0
        cur = 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i-1])
            while cur < n and s[cur] not in occ:
                occ.add(s[cur])
                cur += 1
            max_length = max(max_length, cur-i)
        return max_length


if __name__ == '__main__':
    s = Solution()
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"
    print(s.lengthOfLongestSubstring(s1))
    print(s.lengthOfLongestSubstring(s2))
    print(s.lengthOfLongestSubstring(s3))
    print(s.lengthOfLongestSubstring(""))