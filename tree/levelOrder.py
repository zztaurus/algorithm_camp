
"""

https://leetcode-cn.com/problems/binary-tree-level-order-traversal/


二叉树的层序遍历


"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def levelOrder(self, root):
        """
        广度优先
        时间复杂度: O(n)
        空间复杂度: O(n)
        """

        if not root:
            return []
        queue = [root]
        out = []

        while len(queue) > 0:

            next_level_node = []
            current_level_val = []

            for node in queue:
                current_level_val.append(node.val)
                if node.left:
                    next_level_node.append(node.left)
                if node.right:
                    next_level_node.append(node.right)
            out.append(current_level_val)
            queue = next_level_node

        return out

    def levelOrder_2(self, root):

        """

        DFS


        """

        if not root:
            return []
        queue = [root]
        out = []

        while len(queue) > 0:

            next_level_node = []
            current_level_val = []

            for node in queue:
                current_level_val.append(node.val)
                if node.left:
                    next_level_node.append(node.left)
                if node.right:
                    next_level_node.append(node.right)
            out.append(current_level_val)
            queue = next_level_node

        return out

