

"""

https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

从前序与中序遍历序列构造二叉树

二叉树前序遍历的顺序为：

    先遍历根节点；

    随后递归地遍历左子树；

    最后递归地遍历右子树。

二叉树中序遍历的顺序为：

    先递归地遍历左子树；

    随后遍历根节点；

    最后递归地遍历右子树。


"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def buildTree(self, preorder, inorder):

        """

        递归终止条件的判定: 左右子树为空，也就是前序遍历和后续遍历列表为空

        前序遍历 【根节点，【左子树的前序遍历结果】【右子树的前序遍历结果】】
        中序遍历 【【左子树的中序遍历结果】根节点 【右子树的中序遍历结果】】

        找到左右子树的前序遍历和后续遍历


        """

        pre_len = len(preorder)
        in_len = len(inorder)
        root = self.__build_tree(preorder, 0, pre_len - 1, inorder, 0, in_len-1)
        return root

    def __build_tree(self, preorder, pre_left, pre_right,
                     inorder, in_left, in_right):

        if pre_left > pre_right or in_left > in_right:
            return None

        pivot = preorder[pre_left]
        root = TreeNode(pivot)

        pivot = preorder[pre_left]
        pivot_index = in_left
        while inorder[pivot_index] != pivot:
            pivot_index += 1

        root.left = self.__build_tree(preorder, pre_left + 1, pre_left + pivot_index - in_left,  # pivot_index - in_left 左子树中序遍历长度
                                      inorder, in_left, pivot_index - 1)  # 确定左子树的前序遍历和中序遍历
        root.right = self.__build_tree(preorder, pre_left + pivot_index - in_left + 1, pre_right,
                                       inorder, pivot_index + 1, in_right)  # 确定右子树的前序遍历和中序遍历

        return root











