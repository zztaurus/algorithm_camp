"""

https://leetcode-cn.com/problems/minesweeper/

扫雷游戏

"""

import collections

class Solution(object):

    def updateBoard(self, board, click):

        """
        BFS
        """

        m, n = len(board), len(board[0])
        dx = [0, 1, 0, -1, 1, 1, -1, -1]
        dy = [1, 0, -1, 0, -1, 1, 1, -1]

        def digit(row, col):
            cnt = 0
            for i in range(8):
                nrow, ncol = row + dx[i], col + dy[i]
                if m > nrow >= 0 and n > ncol >= 0 and board[nrow][ncol] == 'M':
                    cnt += 1
            return cnt

        # BFS
        def reveal(row, col):
            cnt = digit(row, col)
            if cnt > 0:
                board[row][col] = str(cnt)
                return
            q = collections.deque()
            q.append((row, col))
            while q:
                row, col = q.popleft()
                cnt = digit(row, col)
                if board[row][col] != 'E':
                    continue
                if cnt > 0:
                    board[row][col] = str(cnt)
                else:
                    board[row][col] = 'B'
                    for i in range(8):
                        nrow, ncol = row + dx[i], col + dy[i]
                        if m > nrow >= 0 and n > ncol >= 0 and board[nrow][ncol] == 'E':
                            q.append((nrow, ncol))

        row, col = click
        if board[row][col] == 'M':
            board[row][col] = 'X'
        else:
            reveal(row, col)
        return board

    def updateBoard_2(self, board, click):

        m, n = len(board), len(board[0])
        dx = [0, 1, 0, -1, 1, 1, -1, -1]
        dy = [1, 0, -1, 0, -1, 1, 1, -1]

        def digit(row, col):
            cnt = 0
            for i in range(8):
                nrow, ncol = row + dx[i], col + dy[i]
                if m > nrow >= 0 and n > ncol >= 0 and board[nrow][ncol] == 'M':
                    cnt += 1
            return cnt

        # DFS
        def reveal(row, col):
            cnt = digit(row, col)
            if cnt == 0:
                board[row][col] = 'B'
                for i in range(8):
                    nrow, ncol = row + dx[i], col + dy[i]
                    if m > nrow >= 0 and n > ncol >= 0 and board[nrow][ncol] == 'E':
                        reveal(nrow, ncol)

            else:
                board[row][col] = str(cnt)

        row, col = click
        if board[row][col] == 'M':
            board[row][col] = 'X'
        else:
            reveal(row, col)
        return board



