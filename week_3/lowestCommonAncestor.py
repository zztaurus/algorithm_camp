"""

https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/

剑指 Offer 68 - II. 二叉树的最近公共祖先

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):


    def lowestCommonAncestor(self, root, p, q):


        """

        1) 如果p为root或者q为root, 那么root为最近公共祖先

        2) 如果 p, q 分不在root节点的异侧，(分别在root的左右子树中)

        3) ancestor 在root节点左子树或者右子树中

        递归解析:


        终止条件：

            1) 当越过叶节点，则直接返回 nullnull

            2) 当root 等于 p, q，则直接返回 root；

        递推工作：

            开启递归左子节点，返回值记为 leftleft ；
            开启递归右子节点，返回值记为 rightright ；

        返回值：

            根据 left_ancestor 和 right_ancestor ，可展开为四种情况；
            1. 当 left_ancestor 和 right_ancestor 同时为空 ：说明 root 的左 / 右子树中都不包含 p,q, 返回 nullnull ；

            2. 当 left_ancestor 和 right_ancestor 同时不为空 ：说明 p, q 分列在 rootroot 的 异侧 （分别在 左 / 右子树），因此 root 为最近公共祖先，返回 root ；

            3. 当 left_ancestor 为空，right_ancestor 不为空 ：p, q  都不在 root 的左子树中，直接返回 right_ancestor 。具体可分为两种情况：

                p,q  其中一个在 root 的 右子树 中，此时 right_ancestor 指向 pp（假设为 pp ）；
                p,q  两节点都在 root 的 右子树 中，此时 right_ancestor 指向 最近公共祖先节点 ；

                当 left_ancestor 不为空 ， right_ancestor 为空 ：与情况 3. 同理；


        时间复杂度： O(n)


        空间复杂度： O(n)

        note: 此题中的递归是对二叉树进行前序遍历，遇到 p 或者 q 返回。

        """

        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root



