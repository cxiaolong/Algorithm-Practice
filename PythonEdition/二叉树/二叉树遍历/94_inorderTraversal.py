from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def in_order(node):
            if node:
                in_order(node.left)
                res.append(node.val)
                in_order(node.right)
        res = []
        in_order(root)
        return res
