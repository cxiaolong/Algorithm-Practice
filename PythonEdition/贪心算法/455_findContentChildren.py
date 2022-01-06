from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # g[i]表示第i个孩子的胃口值
        # s[j]表示第j块饼干的尺寸
        g.sort()
        s.sort()
        res = 0
        for i in range(len(s)-1):
            if res < len(g) and g[res] <= s[i]:
                res += 1
        return res



if __name__ == '__main__':
    g1 = [1, 2, 3]
    s1 = [1, 1]
    g2 = [1, 2]
    s2 = [1, 2, 3]
    s = Solution()
    print(s.findContentChildren(g1, s1))
    print(s.findContentChildren(g2, s2))