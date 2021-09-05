
"""

https://leetcode-cn.com/problems/jump-game-iv/

跳跃游戏 IV

每一步，你可以从下标 i 跳到下标：

    i + 1 满足：i + 1 < arr.length
    i - 1 满足：i - 1 >= 0
    j 满足：arr[i] == arr[j] 且 i != j

"""


class Solution:

    def minJumps(self, nums):

        """
        广度优先遍历，每一层遍历当前所有节点可以跳跃的下一个节点，如果下一个节点可达目标节点，

        时间复杂度: O(n) 一次遍历

        空间复杂度: O(n) 极端情况下 nex 数组中 中包括了除当前节点外的所有节点。
        """
        n = len(nums)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if nums[i] in graph:
                graph[nums[i]].append(i)
            else:
                graph[nums[i]] = [i]

        curs = [0]  # 存储当前层，也就是首个节点，广度优先遍历的首个节点。
        visited = {0}  # 使用visited数组避免重复遍历
        step = 0

        while curs:
            nex = []

            # 遍历当前层
            for node in curs:

                #
                if node == n-1:
                    return step

                # check same value
                for child in graph[nums[node]]:  # 搜索下一层, 使用哈希索引加速找到可以跳跃的下一个目标位置。
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)

                # clear the list to prevent redundant search
                graph[nums[node]] = []

                # check neighbors
                # for child in [node-1, node+1]:
                #     if 0 <= child < len(nums) and child not in visited:
                #         visited.add(child)
                #         nex.append(child)

            curs = nex
            step += 1

        return -1