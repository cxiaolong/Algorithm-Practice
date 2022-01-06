from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 方法1-层序遍历：
class Solution1:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res

        is_left = 1
        queue = [root]
        while queue:
            current_size = len(queue)
            temp = []
            for i in range(current_size):
                cur_node = queue.pop()
                temp.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                     queue.append(cur_node.right)
            res.append(temp[::is_left])
            is_left *= -1
        return res


# 方法2-广度优先搜索+双端队列
class Solution2:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = [root]
        order = True
        while queue:
            current_size = len(queue)
            temp_deque = []   # 用列表模拟双端队列
            for i in range(current_size):
                cur_node = queue.pop()
                if order:
                    temp_deque.append(cur_node.val)
                else:
                    temp_deque.insert(0, cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            res.append(temp_deque)
        return res





if __name__ == '__main__':
    s1 = Solution1()