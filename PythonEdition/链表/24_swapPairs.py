# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 方法1-迭代
class Solution1:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_node = ListNode(next=head)
        cur = dummy_node
        while cur.next and cur.next.next:
            node1 = cur.next
            node2 = cur.next.next
            cur.next = node2
            node1.next = node2.next
            node2.next = node1
            cur = node1
        return dummy_node.next


# 方法2-递归
class Solution2:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or head.next:
            return head
        one = head
        two = head.next
        three = head.next.next

        two.next = one
        one.next = self.swapPairs(three)

        return two
