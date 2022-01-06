class Node:
    """定义单项循环链表的节点"""
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class SingleCircleList:
    """单项循环链表的构造"""
    def __init__(self, head=None):
        self.head = head
        if self.head:
            self.head.next = self.head

    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None

    def length(self):
        """计算链表长度"""
        cur = self.head  # 创建一个指向当前节点的指针
        if not cur:
            return 0
        length = 1
        while cur.next != self.head:
            length += 1
            cur = cur.next
        return length

    def travel(self):
        """遍历链表"""
        cur = self.head  # 创建一个指向当前节点的指针
        if not cur:
            return
        while cur.next != self.head:
            print(cur.value, end=" ")
            cur = cur.next
        print(cur.value)

    def add(self, item):
        """头插法插入元素"""
        node = Node(item)
        if not self.head:
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            # 退出循环时，cur指向最后一个节点
            node.next = self.head
            self.head = node
            cur.next = self.head

    def append(self, item):
        """尾插法插入元素"""
        node = Node(item)
        if not self.head:
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            # 遍历结束时，cur指向最后一个节点
            cur.next = node
            node.next = self.head

    def insert(self, pos, item):
        """指定位置插入元素"""
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            node = Node(item)
            pre = self.head  # 前一节点的引用
            count = 0
            while count < pos-1:
                pre = pre.next
                count += 1
            # 循环结束时，cur指向pos前一位置
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除指定元素"""
        # 前后指针法
        cur = self.head
        pre = None
        while cur != self.head:
            if cur.value == item:
                # 先判断是否是头节点
                if not pre:
                    rear = self.head
                    while rear.next != self.head:
                        rear = rear.next
                    # 退出循环时，rear指向尾节点
                    self.head = cur.next
                    rear.next = self.head
                else:
                    pre.next = cur.next
                return
            pre = cur
            cur = cur.next
        # 退出循环，cur指向尾节点
        if cur.value == item:
            if cur == self.head:
                # 只有一个节点
                self.head = None
            else:
                pre.next = self.head

    def search(self, item):
        """查找指定元素是否存在"""
        cur = self.head
        while cur.next != self.head:
            if cur.value == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    scl = SingleCircleList()