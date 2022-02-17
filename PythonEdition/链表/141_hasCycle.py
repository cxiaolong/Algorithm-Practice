# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 方法1-栈法
class Solution1:
    def hasCycle(self, head: ListNode) -> bool:
        stack = []
        cur = head
        while head:
            stack.append(cur)
            if cur.next in stack:
                return True
            cur = cur.next

        return False


# 方法2-快慢指针法（Floyd判圈算法、龟兔赛跑算法）：当有圈时，快慢指针总会重合
class Solution2:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:  # 当fast或fast的下一步指为空时，说明遍历结束
                return False
            slow = slow.next  # slow每次走一步
            fast = fast.next.next  # fast每次走一步

        return True




if __name__ == '__main__':
    s1 = Solution1()