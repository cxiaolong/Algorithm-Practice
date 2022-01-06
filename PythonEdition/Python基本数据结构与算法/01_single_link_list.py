class Node:
    """定义单向链表的节点"""
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class SingleLinkList:
    """单链表的构造"""
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None

    def length(self):
        """计算链表长度"""
        cur = self.head  # 创建一个指向当前节点的指针
        length = 0
        while cur:
            length += 1
            cur = cur.next
        return length

    def travel(self):
        """遍历链表"""
        cur = self.head  # 创建一个指向当前节点的指针
        while cur:
            print(cur.value, end=" ")
            cur = cur.next
        print()

    def add(self, item):
        """头插法插入元素"""
        node = Node(item)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def append(self, item):
        """尾插法插入元素"""
        node = Node(item)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            # 遍历结束时，cur指向最后一个节点
            cur.next = node

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
        while cur:
            if cur.value == item:
                if not pre:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                    return
            pre = cur
            cur = cur.next

    def search(self, item):
        """查找指定元素是否存在"""
        cur = self.head
        while cur:
            if cur.value == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    sll = SingleLinkList()
    print(sll.is_empty())
    print(sll.length())

    sll.add(1)
    print(sll.is_empty())
    print(sll.length())
    sll.travel()