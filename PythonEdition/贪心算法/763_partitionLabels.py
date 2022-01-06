from typing import List


# 方法1-贪心算法
class Solution1:
    def partitionLabels(self, s: str) -> List[int]:
        last = [0] * 26
        for i, ch in enumerate(s):
            last[ord(ch) - ord('a')] = i
        partition = []
        start = end = 0
        for i, ch in enumerate(s):
            end = max(end, last[ord(ch) - ord('a')])
            if i == end:
                partition.append(end-start+1)
                start = end + 1
        return partition



if __name__ == '__main__':
    S = "ababcbacadefegdehijhklij"
    s1 = Solution1()
    print(s1.partitionLabels(S))