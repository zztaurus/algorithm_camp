
"""




"""


class Solution(object):

    def jump(self, nums):

        """
        寻找下一步可达的最远位置。

        维护当前能够到达的最大下标位置，记为边界。我们从左到右遍历数组，到达边界时，更新边界并将跳跃次数增加 1。

        O(n)
        O(1)

        """

        n = len(nums)
        maxPos, end, step = 0, 0, 0

        for i in range(n - 1):

            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos # 更新每次跳跃可达的最远边界，当到达最远边界，进入下次跳跃。
                    step += 1
