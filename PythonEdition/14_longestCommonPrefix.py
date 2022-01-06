from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        n = len(strs)
        for i in range(1, len(strs[0])):
            common_prefix = strs[0][0:i]

            for j in range(1, n):
                if strs[j][0:i] != common_prefix:
                    return strs[0][0: i - 1]


if __name__ == '__main__':
    s = Solution()
    strs1 = ["flower", "flow", "flight"]
    strs2 = ["dog", "racecar", "car"]
    strs3 = [""]

    print(s.longestCommonPrefix(strs1))
    print(s.longestCommonPrefix(strs2))
    print(s.longestCommonPrefix(strs3))

