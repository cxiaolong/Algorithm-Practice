from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def pre_order(node):
            if node:
                res.append(node.val)
                pre_order(node.left)
                pre_order(node.right)
        res = []
        pre_order(root)
        return res
