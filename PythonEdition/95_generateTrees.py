from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generate_trees(start, end):
            if start > end:
                return [None, ]
            all_trees = []
            for i in range(start, end+1):  # 枚举可行根节点
                # 获得所有的可行左子树的集合
                left_trees = generate_trees(start, i-1)
                # 获取所有可行的右子树
                right_trees = generate_trees(i+1, end)

                # 从左子树中选择一个树，右子树中选择一个树，拼接到根节点
                for l in left_trees:
                    for r in right_trees:
                        curr_tree = TreeNode(i)
                        curr_tree.left = l
                        curr_tree.right = r
                        all_trees.append(curr_tree)
            return all_trees

        return generate_trees(1, n)


if __name__ == '__main__':
    s = Solution()
    print(s.generateTrees(3))
