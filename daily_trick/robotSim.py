
"""

https://leetcode-cn.com/problems/walking-robot-simulation/

模拟行走机器人

"""


class Solution(object):

    def robotSim(self, commands, obstacles):
        """

        时间复杂度: O(N + K) N,K 分别是 commands 和 obstacles 的长度
        空间复杂度: O(K)
        """

        dx = [0, 1, 0, -1]  # n, e, s, w
        dy = [1, 0, -1, 0]  # n, e, s, w
        x = y = direct = 0
        obstacle_set = set(map(tuple, obstacles))
        ans = 0

        for cmd in commands:
            if cmd == -2:  # left
                direct = (direct - 1) % 4  # 0, 1, 2, 3
            elif cmd == -1:  # right
                direct = (direct + 1) % 4
            else:
                for k in range(cmd):
                    if (x + dx[direct], y + dy[direct]) not in obstacle_set:
                        x += dx[direct]
                        y += dy[direct]
                        ans = max(ans, x * x + y * y)

        return ans


