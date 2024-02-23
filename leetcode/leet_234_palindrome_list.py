# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head is None:
            return True

        slow, fast = head, head
        while slow and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow=slow.next

        left, right = head, self.reverse(slow)
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


    def reverse(self, head):
        pre, cur = None, head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre