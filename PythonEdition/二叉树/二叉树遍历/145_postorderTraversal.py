from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def poster_order(root: TreeNode):
            if root:
                poster_order(root.left)
                poster_order(root.right)
                res.append(root.val)

        res = []
        poster_order(root)
        return res
