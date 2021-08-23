
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


import copy

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

        return [item for item in out[::-1]]

    def levelOrder_2(self, root):

        """

        深度优先：

        时间复杂度：O(N)
        空间复杂度：O(N)

        """

        if not root: return []
        level_out = {}
        self.dfs(root, 0, level_out)
        res = [val for val in level_out.values()[::-1]]
        return res

    def dfs(self, root, index, level_out):

        if not root:
            return

        if index not in level_out:
            level_out.update({index: []})

        level_out[index].append(root.val)

        if root.left:
            self.dfs(root.left, index + 1, level_out)
        if root.right:
            self.dfs(root.right, index + 1, level_out)







