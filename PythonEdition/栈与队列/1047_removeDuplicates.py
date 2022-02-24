# 使用栈
class Solution1:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)


# 方法2-双指针
class Solution2:
    def removeDuplicates(self, s: str) -> str:
        res = list(s)
        length = len(s)
        slow = fast = 0
        while fast < length:
            # slow指向的值替换为fast指向的值
            res[slow] = res[fast]

            if slow > 0 and res[slow] == res[slow - 1]:  # 去除相邻重复项
                slow -= 1
            else:
                slow += 1
            fast += 1
        return "".join(res[0: slow])


if __name__ == '__main__':
    s1 = "abbaca"
    s2 = "azxxzy"
    so1 = Solution1()
    so2 = Solution2()
    print(so1.removeDuplicates(s1))
    print(so1.removeDuplicates(s2))
    print(so2.removeDuplicates(s1))
    print(so2.removeDuplicates(s2))
