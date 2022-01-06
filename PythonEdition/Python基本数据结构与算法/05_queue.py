class Queue:
    """用列表构建队列结构"""
    def __init__(self):
        self.__items = []

    def enqueue(self, item):
        """向队列中添加元素"""
        self.__items.insert(0, item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        return self.__items.pop()

    def is_empty(self):
        """判断队列是否为空"""
        return self.__items == []

    def size(self):
        """计算队列长度"""
        return len(self.__items)



if __name__ == '__main__':
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())