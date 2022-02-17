from collections import Counter, defaultdict


# 方法1-使用list记录magazine中每个字符的个数
class Solution1:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record = [0] * 26
        for i in magazine:
            # 并不需要记住字符a的ASCII，只要求出一个相对数值就可以了
            record[ord(i) - ord('a')] += 1
        for j in ransomNote:
            if record[ord(j) - ord('a')] == 0:
                return False
            record[ord(j) - ord('a')] -= 1
        return True


# 方法2-利用Counter计数器计数字符
class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_r = Counter(ransomNote)
        counter_m = Counter(magazine)
        for i in counter_r.keys():
            if counter_r[i] > counter_m[i]:
                return False
        return True


# 方法3-利用defaultdict计数字符
class Solution3:
    def canConstruct(self, randomNote: str, magazine: str) -> bool:
        char_count = defaultdict(int)
        for i in magazine:
            char_count[i] += 1

        for j in randomNote:
            if char_count[j] == 0:
                return False
            char_count[j] -= 1
        return True


if __name__ == '__main__':
    ransomNote1 = "a"
    magazine1 = "b"
    ransomNote2 = "aa"
    magazine2 = "ab"
    ransomNote3 = "aa"
    magazine3 = "aab"
    s1 = Solution1()
    s2 = Solution2()
    s3 = Solution3()
    print(s1.canConstruct(ransomNote1, magazine1))
    print(s1.canConstruct(ransomNote2, magazine2))
    print(s1.canConstruct(ransomNote3, magazine3))
    print(s2.canConstruct(ransomNote1, magazine1))
    print(s2.canConstruct(ransomNote2, magazine2))
    print(s2.canConstruct(ransomNote3, magazine3))
    print(s3.canConstruct(ransomNote1, magazine1))
    print(s3.canConstruct(ransomNote2, magazine2))
    print(s3.canConstruct(ransomNote3, magazine3))