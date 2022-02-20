# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 方法1-栈法：利用栈先进后出反转链表
class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        dummy_node = ListNode(0)
        pointer = dummy_node
        while stack:
            pointer.next = stack.pop()
            pointer = pointer.next
        # 循环结束时，链表反转完成
        # 最后注意要将最后一个节点的next域置空
        pointer.next = None
        return dummy_node.next


# 方法2-迭代法（前后指针法）：
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            poster = cur.next  # 保存cur后一个节点的链接状态
            cur.next = pre
            pre = cur
            cur = poster
        return pre


# 方法3-递归法：
class Solution3:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return p


if __name__ == '__main__':
    s1 = Solution1()
