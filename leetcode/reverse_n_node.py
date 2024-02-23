
"""

翻转前N个节点

"""

class Solution(object):

    def reverseList_N(self, head, n):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        global dst_node
        if n == 1:
            dst_node = head
            return
        last = self.reverseList_N(head.next)
        head.next.next = head
        head.next = dst_node
        return last
