from operator import add, sub, mul
from typing import List


class Solution1:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators_fn = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": lambda x, y: int(x / y)
        }
        for ch in tokens:
            if ch not in operators_fn:
                stack.append(int(ch))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                num = operators_fn[ch](num1, num2)
                stack.append(num)
        return stack[-1]


class Solution2:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for ch in tokens:
            if ch not in operators:
                stack.append(ch)
            else:
                num2, num1 = stack.pop(), stack.pop()
                num = int(eval(f"{num1}{ch}{num2}"))
                stack.append(num)
        return int(stack[-1])


if __name__ == '__main__':
    tokens1 = ["2", "1", "+", "3", "*"]
    tokens2 = ["4", "13", "5", "/", "+"]
    tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    s1 = Solution1()
    s2 = Solution2()
    print(s1.evalRPN(tokens1))
    print(s1.evalRPN(tokens2))
    print(s1.evalRPN(tokens3))
    print(s2.evalRPN(tokens1))
    print(s2.evalRPN(tokens2))
    print(s2.evalRPN(tokens3))
