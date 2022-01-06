class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 方法1-层次遍历：模拟下楼梯，每下一层楼梯才计算楼梯阶数，否则只遍历不计数
class Solution1:
    def maxDepth(self, root: TreeNode) -> int:
        height = 0
        if not root:
            return height
        queue = [root]
        while queue:
            currentSize = len(queue)
            for i in range(currentSize):  # 循环用于控制层数，循环结束，则表明该层的所有节点均走完
                cur_node = queue.pop(0)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            height += 1
        # 当队列为空时，表明所有层数均走完
        return height


# 方法2-深度优先搜索：将树分为左子树和右子数，分别计算子树的高度，则这是一个递归问题，递归终止条件是子树节点为空
class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1



if __name__ == '__main__':
    s1 = Solution1()