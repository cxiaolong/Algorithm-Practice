class Node:
    """二叉树的节点表示"""
    def __init__(self, val=-1, lchild=None, rchild=None):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    """二叉树"""
    def __init__(self, root=None):
        self.root = root

    def add(self, item):
        """向二叉树中添加节点"""
        node = Node(item)
        if not self.root:
            self.root = node
        else:
            queue = [self.root]
            # 对队列中已有节点进行层次遍历
            while queue:
                # 弹出队列中的首元素
                cur = queue.pop(0)
                if not cur.lchild:
                    cur.lchild = node
                    return
                else:
                    queue.append(cur.lchild)
                if not cur.rchild:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.rchild)


    def breadth_travel(self):
        """二叉树的广度遍历"""
        if not self.root:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.val, end=" ")
            if cur_node.lchild:
                queue.append(cur_node.lchild)
            if cur_node.rchild:
                queue.append(cur_node.rchild)


    def preorder(self, node):
        """二叉树的先序遍历"""
        if not node:
            return
        print(node.val, end=" ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)


    def inorder(self, node):
        """中序遍历"""
        if not node:
            return
        self.inorder(node.lchild)
        print(node.val, end=" ")
        self.inorder(node.rchild)

    def postorder(self, node):
        """后序遍历"""
        if not node:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.val, end=" ")



if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(" ")
    tree.preorder(tree.root)
    print(" ")
    tree.inorder(tree.root)
    print(" ")
    tree.postorder(tree.root)
    print(" ")