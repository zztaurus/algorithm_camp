
"""

二叉树的深度

https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/submissions/


"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def solution_1(self, root):

        """

        递归法

        时间复杂度 O(n)

        思路: DFS
        找出终止条件：当前节点为空
        找出返回值：节点为空时说明高度为 0，所以返回 0；节点不为空时则分别求左右子树的高度的最大值，同时加1表示当前节点的高度，返回该数值

        时间复杂度：O(n)O(n)，其中 nn 为二叉树节点的个数。每个节点在递归中只被遍历一次。

        空间复杂度：O(height)  O(height)，其中 height 表示二叉树的高度。递归函数需要栈空间，而栈空间取决于递归的深度，因此空间复杂度等价于二叉树的高度。

        """

        if not root:

            return 0

        return max(self.solution_1(root.left), self.solution_1(root.right)) + 1

    def solution_2(self, root):

        """

        迭代法

        思路：BFS, 使用队列

        队列中存储当前层的所有节点，当当前层的所有节点出队后，则树的深度加1


        """

        if not root:
            return 0

        from collections import deque
        d = deque()
        depth = 0
        d.append(root)
        while len(d) > 0:

            size = len(d)
            while size > 0:
                node = d.popleft()
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
                size -= 1

            depth += 1

        return depth











