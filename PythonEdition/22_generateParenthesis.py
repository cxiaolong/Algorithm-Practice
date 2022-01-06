from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                res.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        res = []
        backtrack([], 0, 0)
        return res


if __name__ == '__main__':
    n1 = 3
    n2 = 1
    s = Solution()
    print(s.generateParenthesis(n1))
    print(s.generateParenthesis(n2))
