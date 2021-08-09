# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


"""
环形链表

https://leetcode-cn.com/problems/linked-list-cycle/
"""

class HasCycle(object):

    def solution_1(self, head):
        """
        解法一: 使用hash表记录已经访问过的链表节点，如果又换存在，那必然存在节点后续或继续访问到
        """

        seen = set()

        while head is not None:
            if head in seen:
                return True
            seen.add(head)
            head = head.next

        return False

    def solution_2(self, head):

        """
        解法二:  快慢指针法，
        """

        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True







