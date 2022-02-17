from collections import Counter, defaultdict


# 方法1-利用列表作为哈希表
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        record = [0] * 26
        for i in s:
            # 并不需要记住字符a的ASCII，只要求出一个相对数值就可以了
            record[ord(i) - ord('a')] += 1
        for j in t:
            record[ord(j) - ord('a')] -= 1

        for item in record:
            if item != 0:
                return False

        return True


# 方法2-利用Counter计数器计数字符
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = Counter()
        for i in s:
            counter[i] += 1
        for j in t:
            counter[j] -= 1
            if counter[j] == 0:
                del counter[j]

        return True if len(counter) == 0 else False


# 方法3-直接初始化计数器
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)


# 方法4-利用defaultdict计数字符
class Solution4:
    def isAnagram(self, s: str, t: str) -> bool:
        char_s = defaultdict(int)
        char_t = defaultdict(int)

        for i in s:
            char_s[i] += 1

        for j in t:
            char_t[j] += 1

        return char_s == char_t


if __name__ == '__main__':
    s1 = "anagram"
    t1 = "nagaram"
    s2 = "rat"
    t2 = "car"
    so1 = Solution1()
    so2 = Solution2()
    so3 = Solution3()
    so4 = Solution4()
    print(so1.isAnagram(s1, t1))
    print(so1.isAnagram(s2, t2))
    print(so2.isAnagram(s1, t1))
    print(so2.isAnagram(s2, t2))
    print(so3.isAnagram(s1, t1))
    print(so3.isAnagram(s2, t2))
    print(so4.isAnagram(s1, t1))
    print(so4.isAnagram(s2, t2))