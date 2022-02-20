class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 方法1-两次遍历：先遍历计算出链表长度l，再遍历到第l-n+1的位置，删除该位置节点
class Solution1:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 先遍历计算链表长度
        cur1 = head
        length = 0
        while cur1:
            length += 1
            cur1 = cur1.next
        # 循环结束时，cur指向最后一个节点，lenth代表链表长度

        # 哑节点法：添加了哑节点，那么头节点的前驱节点就是哑节点本身
        dummy_node = ListNode(0, head)
        cur2 = dummy_node
        # 第二次循环，找到length-n+1的位置，即为要删除的元素
        for i in range(1, length - n + 1):
            cur2 = cur2.next
        # 退出循环时，cur2指向待删除元素
        cur2.next = cur2.next.next
        return dummy_node.next


# 方法2-栈法：利用栈先进后出的特点，从末尾逐一取出元素，当取出的元素是倒数n时，删除元素
class Solution2:
    def removeNthFormEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_node = ListNode(0, next=head)  # 构造哑节点，避免分类讨论
        # 构造栈结构，充当盛装节点的容器
        stack = []
        cur = dummy_node
        while cur:
            stack.append(cur)
            cur = cur.next
        for i in range(n):
            stack.pop()
        prev = stack[-1]  # 待删除节点的前一节点
        prev.next = prev.next.next
        return dummy_node.next


# 方法三-前后指针法：指针first与指针second相距n，当后指针first遍历到链表尾部，则second指向待删除的节点
class Solution3:
    def removeNthFormEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_node = ListNode(0, next=head)
        first = head
        second = dummy_node

        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next
        # 循环结束时，second指向待删除节点的前一节点
        second.next = second.next.next
        return dummy_node.next


if __name__ == '__main__':
    s1 = Solution1()
    s2 = Solution2()
    s1.removeNthFromEnd()
