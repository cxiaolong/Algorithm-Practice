# 方法1-重构字符串
class Solution1:
    """
    time complexity：O(m+n) 我们需要对2各字符串各遍历一次
    space complexity: O(m+n) 重建2个字符串的开销
    """
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s: str) -> str:
            ret = list()
            for c in s:
                if c != '#':
                    ret.append(c)
                elif ret:
                    ret.pop()
            return "".join(ret)
        return build(s) == build(t)


# 方法2-双指针法-逆序遍历
class Solution2:
    def backspaceCompare(self, s: str, t: str) -> bool:

        pass


if __name__ == '__main__':
    s1 = "ab#c"
    t1 = "ad#c"
    s2 = "ab##"
    t2 = "c#d#"
    s3 = "a#c"
    t3 = "b"
    so1 = Solution1()
    print(so1.backspaceCompare(s1, t1))
    print(so1.backspaceCompare(s2, t2))
    print(so1.backspaceCompare(s3, t3))
