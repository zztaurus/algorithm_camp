
"""


https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/


剑指 Offer 59 - I. 滑动窗口的最大值


"""

import collections


class Solution(object):

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if not nums or k == 0: return []
        deque = collections.deque()

        for i in range(k):
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        res = [deque[0]]

        for i in range(k, len(nums)):
            if deque[0] == nums[i - k]:  # nums[i - k] 上一个窗口的第一个元素, 如果上一个窗口的第一个元素还在deque中, 则将该元素移除。
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res
