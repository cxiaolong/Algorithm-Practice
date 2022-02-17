# Definition for single-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = ListNode()  # 哨兵节点
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        while cur:
            if index == -1:
                return cur.val
            index -= 1
            cur = cur.next

    def addAtHead(self, val: int) -> None:
        return self.addAtIndex(index=0, val=val)

    def addAtTail(self, val: int) -> None:
        return self.addAtIndex(index=self.size, val=val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        pre = self.head
        while pre:
            if index == 0:
                temp = pre.next
                pre.next = ListNode(val=val, next=temp)
                self.size += 1
                return
            index -= 1
            pre = pre.next

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size:
            return
        pre = self.head
        while pre.next:
            if index == 0:
                pre.next = pre.next.next
                self.size -= 1
                return
            else:
                index -= 1
                pre = pre.next


if __name__ == '__main__':
    linkedList = MyLinkedList()
    linkedList.addAtHead(1)
    linkedList.addAtTail(3)
    linkedList.addAtIndex(1, 2)  # 链表变为1-> 2-> 3
    linkedList.get(1)  # 返回2
    linkedList.deleteAtIndex(1)  # 现在链表是1-> 3
    linkedList.get(1)



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)