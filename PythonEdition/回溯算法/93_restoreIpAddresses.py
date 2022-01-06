from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(p):
            if (p == '0') or (p[0] != '0' and 0 < int(p) < 256):
                return True
            return False

        def backtrack(s, path, start_index):
            if len(s) > 12:
                return
            if len(path) == 4 and start_index == len(s):
                res.append(".".join(path.copy()))
            for i in range(start_index, len(s)):
                if len(s) - start_index > 3 * (4 - len(path)):  # 剪枝，剩余的字符串长度大于允许的最大长度则跳过
                    continue
                p = s[start_index:i + 1]
                if is_valid(p):
                    path.append(p)
                    backtrack(s, path, i + 1)
                    path.pop()

        res = []
        backtrack(s, [], 0)
        return res


if __name__ == '__main__':
    s1 = "25525511135"
    s2 = "0000"
    s3 = "1111"
    s4 = "010010"
    s5 = "101023"
    s = Solution()
    print(s.restoreIpAddresses(s1))
    print(s.restoreIpAddresses(s2))
    print(s.restoreIpAddresses(s3))
    print(s.restoreIpAddresses(s4))
    print(s.restoreIpAddresses(s5))
