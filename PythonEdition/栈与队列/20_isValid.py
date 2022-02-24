# 方法1-使用栈
class Solution1:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(":
                stack.append(")")
            elif i == "[":
                stack.append("]")
            elif i == "{":
                stack.append("}")
            else:
                if not stack or stack[-1] != i:
                    return False
                stack.pop()

        return not stack


# 方法2-使用栈
class Solution2:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for item in s:
            if item in pairs:
                if not stack or stack[-1] != pairs[item]:
                    return False
                stack.pop()
            else:
                stack.append(item)
        return not stack


if __name__ == '__main__':
    so1 = Solution1()
    so2 = Solution2()
    s1 = "()"
    s2 = "()[]{}"
    s3 = "(]"
    print(so1.isValid(s1))
    print(so1.isValid(s2))
    print(so1.isValid(s3))
    print(so2.isValid(s1))
    print(so2.isValid(s2))
    print(so2.isValid(s3))
