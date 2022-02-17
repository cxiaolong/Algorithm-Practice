from typing import List
from collections import defaultdict


# 排序
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            mp[key].append(word)

        return list(mp.values())


# 计数
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for word in strs:
            counts = [0] * 26
            for c in word:
                counts[ord(c) - ord('a')] += 1
            # 需要将 counter 转换成 tuple 才能进行哈希
            mp[tuple(counts)].append(word)

        return list(mp.values())


if __name__ == '__main__':
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs2 = [""]
    strs3 = ["a"]
    s1 = Solution1()
    s2 = Solution2()
    print(s1.groupAnagrams(strs1))
    print(s1.groupAnagrams(strs2))
    print(s1.groupAnagrams(strs3))
    print(s2.groupAnagrams(strs1))
    print(s2.groupAnagrams(strs2))
    print(s2.groupAnagrams(strs3))