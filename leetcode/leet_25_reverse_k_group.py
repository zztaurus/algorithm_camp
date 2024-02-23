
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        a, b = head
        for i in range(k):
            if not b:
                return head
            b = b.next
        new_head = self.reverse(a, b) # 此时的b已经是第k+1个元素
        a.next = self.reverseKGroup(b, k)
        return new_head

    def reverse(self, a, b):
        pre = None
        cur = a
        while(cur != b):
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre


