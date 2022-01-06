# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 方法1-递归法（前序遍历）
class Solution1:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = root.right, root.left  # 中
            self.invertTree(root.left)  # 左
            self.invertTree(root.right)  # 右
        return root


# 方法2-迭代法（广度优先遍历）
class Solution2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            from collections import deque
            queue = deque([root])
            while queue:
                for i in range(len(queue)):
                    node = queue.popleft()
                    node.left, node.right = node.right, node.left  # 节点处理
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        return root

