from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        left, right = 0, n-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    so = Solution()
    s1 = ["h", "e", "l", "l", "o"]
    s2 = ["H", "a", "n", "n", "a", "h"]
    so.reverseString(s1)
    so.reverseString(s2)
    print(s1)
    print(s2)
