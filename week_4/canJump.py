
"""
https://leetcode-cn.com/problems/jump-game/


跳跃游戏


"""


class Solution(object):

    def canJump(self, nums):
        """
        贪心算法

        要点: 依次遍历数组中的每一个位置，并实时维护 最远可以到达的位置。对于当前遍历到的位置 xx，如果它在 最远可以到达的位置 的范围内，

             那么我们就可以从起点通过若干次跳跃到达该位置，因此我们可以用 x + nums[x] 更新 最远可以到达的位置。

        时间复杂度: O(n)

        空间复杂度: O(1)

        """

        n, max_i = len(nums), 0
        for i in range(n):
            if i <= max_i: # 只有最远最大位置大于等于i, 才满足继续向后寻找最远可达位置的条件。
                max_i = max(max_i, i + nums[i])
                if max_i > n - 1:
                    return True
        return False