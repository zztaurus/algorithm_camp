
"""

给一个索引区间 [m, n]（索引从 1 开始），仅仅反转区间中的链表元素。

"""


class Solution(object):


    def reverse_between(self, head, m, n):

        if m == 1:
            return self.reverseList_N(head, n)
            # 前进到反转的起点触发 base case
        head.next = self.reverse_between(head.next, m - 1, n - 1)
        return head

    def reverseList_N(self, head, n):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        global dst_node
        if n == 1:
            dst_node = head
            return
        last = self.reverseList_N(head.next, n-1)
        head.next.next = head
        head.next = dst_node
        return last
