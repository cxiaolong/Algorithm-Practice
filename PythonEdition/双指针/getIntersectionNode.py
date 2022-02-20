from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 方法1-该方法超出时间限制(43/45)
class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur_A = headA
        cur_B = headB
        nodes_A = []
        while cur_A:
            nodes_A.append(cur_A)
            cur_A = cur_A.next
        while cur_B:
            if cur_B in nodes_A:
                return cur_B
            cur_B = cur_B.next
        return None


# 方法2-你变成我，我变成你，我们便相遇了
class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur_a = headA
        cur_b = headB

        # 假设headA节点数为a，headB节点数为b，公共节点数为c
        # cur1走完一遍headA，第二遍从HeadB走到第一个公共节点的长度为a+(b-c)，同理cur2走了b+(a-c)，cur1与cur2相遇了
        # 当不存在公共节点时，c=0，cur1走到了headB尾节点的next(None)，cur2走到了headA尾节点的next(None)
        while cur_a != cur_b:
            cur_a = cur_a.next if cur_a else headB
            cur_b = cur_b.next if cur_b else headA
        return cur_a