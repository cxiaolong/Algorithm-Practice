from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        results = []
        if root:
            from collections import deque
            que = deque([root])
            while que:
                size = len(que)
                result = []
                for i in range(size):
                    cur = que.popleft()
                    result.append(cur.val)
                    if cur.left:
                        que.append(cur.left)
                    if cur.right:
                        que.append(cur.right)
                results.append(result)
        return results
