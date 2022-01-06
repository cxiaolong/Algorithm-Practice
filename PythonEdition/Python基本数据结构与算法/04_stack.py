class Stack:
    """用列表实现栈结构"""
    def __init__(self):
        self.__items = []

    def is_empty(self):
        """判断栈是否为空"""
        return self.__items == []

    def push(self, item):
        """压栈"""
        self.__items.append(item)

    def pop(self):
        """出栈"""
        return self.__items.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__items:
            return self.__items[-1]
        return None

    def size(self):
        """返回栈的元素个数"""
        return len(self.__items)



if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    stack.push("hello")
    stack.push("world")
    stack.push("itcast")
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())