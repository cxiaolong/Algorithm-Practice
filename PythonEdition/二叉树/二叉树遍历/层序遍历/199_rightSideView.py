from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if root:
            from collections import deque
            que = deque([root])
            while que:
                node = que[-1]  # 每次都取最后一个就行
                res.append(node.val)

                # 获取下一层所有的节点
                for i in range(len(que)):
                    node = que.popleft()
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)
        return res