# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):

    def reverseList_recur(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head
        last = self.reverseList_recur(head.next)
        head.next.next = head
        head.next = None
        return last


    def reverseList_iter(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        while(cur != None):
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre


