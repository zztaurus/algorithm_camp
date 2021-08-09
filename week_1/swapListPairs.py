# Definition for singly-linked list.

"""

两两交换链表节点

"""

class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        递归法
        """

        if head is None or head.next is None:
            return head

        newhead = head.next
        head.next = self.swapPairs(head.next.next)
        newhead.next = head
        return newhead

    def swapPairs2(self, head):

        """
        迭代法
        :param head:
        :return:
        """

        if head is None or head.next is None:
            return head

        wallker = head
        last = None
        pre = wallker.next

        while wallker and wallker.next:
            next_wallker = wallker.next.next
            tmp = wallker.next
            tmp.next = wallker
            last = wallker
            wallker = next_wallker

        if wallker:
            last.next = wallker

        return pre

