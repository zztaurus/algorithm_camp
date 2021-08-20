
"""

https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/


剑指 Offer 06. 从尾到头打印链表


思路一: 递归或者使用栈

思路二:

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def reversePrint(self, head):

        """
        递归

        时间复杂度 O(n)
        空间复杂度 O(n)

        """

        return self.reversePrint(head.next) + [head.val] if head else []

    def reversePrint_2(self, head):

        """
        栈

        时间复杂度 O(n)
        空间复杂度 O(n)

        """

        if not head: return []
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]
