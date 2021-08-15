"""

https://leetcode-cn.com/problems/sliding-window-maximum/

滑动窗口类型题目，使用队列解决

"""


class MaxSlidingWindow(object):

    def solution_1(self, nums, k):

        """
        暴力法 O ( n * k)
        """

        res = []

        for i in range(k, len(nums)+1):
            j = i - k
            res.append(max(nums[j:i]))
        return res

    def solution_2(self, nums, k):
        """

        优先队列

        """
        import heapq
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans

    def solution_3(self, nums, k):
        """
        双端队列
        """
        import collections
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, len(nums)):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])

        return ans


if __name__ == '__main__':
    m = MaxSlidingWindow()
    m.solution_1([1,3,-1,-3,5,3,6,7], 3)




