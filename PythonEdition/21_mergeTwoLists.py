class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 方法1-递归法：
class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# 方法2-迭代法：新建一个空链表，依次往里面装入节点
class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre = ListNode(-1)
        l = pre
        while l1 and l2:
            if l1.val <= l2.val:
                l.next = l1
                l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
            # 移动指针
            l = l.next

        # 最终，l1和l2最多还有一个未被合并，直接将链表尾部指向未被合并完的链表
        l.next = l1 if l1 else l2
        return pre.next



if __name__ == '__main__':
    l3 = ListNode(3)
    l2 = ListNode(2, next=l3)
    l1 = ListNode(1, next=l2)

    l6 = ListNode(5)
    l5 = ListNode(2, next=l6)
    l4 = ListNode(1, next=l5)

    s1 = Solution1()
    s2 = Solution2()
    print(s1.mergeTwoLists(l1, l4))
    print(s2.mergeTwoLists(l1, l4))