"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""

https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/


N 叉树的前序遍历

"""


class Solution(object):

    def preorder(self, root):
        """
        递归法

        时间复杂度: O(n)

        空间复杂度: O(n)
        """

        res = []

        def pre_order(root):

            if root:
                res.append(root.val)
                for node in root.children:
                    pre_order(node)
            return res

        pre_order(root)
        return res

    def preorder_2(self, root):

        """

        迭代法
        """

        if root is None:
            return []
        stack, res = [root, ], []
        while stack:
            root = stack.pop()
            res.append(root.val)
            stack.extend(root.children[::-1])  # 倒序放入 正序取出

        return res

