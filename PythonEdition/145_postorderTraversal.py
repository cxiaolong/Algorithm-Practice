from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 方法1-递归：
class Solution1:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def poster_travel(root):
            if not root:  # 递归的终止条件
                return
            poster_travel(root.left)
            poster_travel(root.right)
            res.append(root.val)

        res = []
        poster_travel(root)
        return res


# 方法2-迭代
class Solution2:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        res = []
        pre = None
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == pre:
                res.append(root.val)
                pre = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return res


if __name__ == '__main__':
    s1 = Solution1()