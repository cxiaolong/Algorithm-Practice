from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 方法1-迭代解法
class Solution1:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
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
        return results[::-1]


# 方法2-递归解法
class Solution2:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        pass
