# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        迭代法
        """

        prehead = ListNode(-1)
        prev = prehead

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        if l1: prev.next = l1

        if l2: prev.next = l2

        return prehead.next

    def mergeTwoLists2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        递归法
        """

        if l1 is None:
            return l1
        elif l2 is None:
            return l2
        else:

            if l1.val <= l2.val:
                l1.next = self.mergeTwoLists2(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists2(l1, l2.next)
                return l2

