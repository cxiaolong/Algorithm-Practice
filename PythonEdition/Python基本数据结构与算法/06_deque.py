class Deque:
    """双端队列"""
    def __init__(self):
        self.__item = []

    def add_front(self, item):
        """队列首部添加元素"""
        self.__item.insert(0, item)

    def add_rear(self, item):
        """队列尾部添加元素"""
        self.__item.append(item)

    def pop_front(self):
        """队列首部删除元素"""
        return self.__item.pop(0)

    def pop_rear(self):
        """队列尾部删除元素"""
        return self.__item.pop()

    def is_empty(self):
        """判断链表是否为空"""
        return self.__item == []

    def size(self):
        """返回队列长度"""
        return len(self.__item)


if __name__ == '__main__':
    deque = Deque()
    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(3)
    deque.add_rear(4)
    print(deque.size())
    print(deque.pop_front())
    print(deque.pop_front())
    print(deque.pop_rear())
    print(deque.pop_rear())