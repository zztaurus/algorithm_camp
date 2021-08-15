
"""

https://leetcode-cn.com/problems/binary-tree-preorder-traversal/

二叉树的前序遍历

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def preorderTraversal(self, root):

        """

        时间复杂度：O(n) ，其中 nn 为二叉树节点的个数。二叉树的遍历中每个节点会被访问一次且只会被访问一次。

        空间复杂度：O(n) 。空间复杂度取决于递归的栈深度，而栈深度在二叉树为一条链的情况下会达到 O(n) 的级别。

        """
        res = []
        self.preorder(root, res)
        return res

    def preorder(self, root, res):

        if not root:
            return
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)


    def preorderTraversal_3(self, root):

        """

        颜色标记法: 利用栈先进后出的特性，模拟中序遍历过程中树的节点的访问过程
        :param root:
        :return:
        """

        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
                stack.append((GRAY, node))
            else:
                res.append(node.val)
        return res


