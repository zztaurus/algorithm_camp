"""

https://leetcode-cn.com/problems/number-of-islands/


岛屿数量


遇到一个岛屿，就将它摧毁


"""

import collections


class Solution(object):

    def numIslands(self, grid):

        """
        DFS

        时间复杂度：O(MN)，其中 M 和 N 分别为行数和列数。最坏情况下整个网格均为陆地, 要访问所有的网格。

        空间复杂度：O(MN)，在最坏情况下，整个网格均为陆地，深度优先搜索的深度达到 MN。

        """
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])

        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j, n, m)
        return count

    def dfs(self, grid, i, j, n, m):

        if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] != '1':
            return

        grid[i][j] = '0'
        self.dfs(grid, i + 1, j, n, m)
        self.dfs(grid, i - 1, j, n, m)
        self.dfs(grid, i, j + 1, n, m)
        self.dfs(grid, i, j - 1, n, m)

    def numIslands_2(self, grid):

        """

        BFS

        广度优先遍历当前island中的所有网格为'1'的值

        时间复杂度: O(MN)
        空间复杂度: O(min(M,N))，在最坏情况下，整个网格均为陆地，队列的大小可以达到 min(M,N)。

        """
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = "0"
                    neighbors = collections.deque([(r, c)])
                    while neighbors:
                        """ 遍历当前island中所有值为1的网格 """
                        row, col = neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                                neighbors.append((x, y))
                                grid[x][y] = "0"
        return num_islands