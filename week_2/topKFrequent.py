
"""

https://leetcode-cn.com/problems/top-k-frequent-elements/

前 K 个高频元素

"""


class Solution(object):

    def topKFrequent(self, nums, k):
        """

        统计各个元素出现的频次，然后放入大顶堆中，返回前k个元素


        """
        import collections
        import heapq
        count = collections.Counter(nums)
        heap = [(val, key) for key, val in count.items()]
        return [item[1] for item in heapq.nlargest(k, heap)]


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    s = Solution()
    s.topKFrequent(nums, 2)