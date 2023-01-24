from collections import deque


class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        cells = [None] * (n ** 2 + 1)

        # mark row col of each label
        label = 1
        columns = list(range(0, n))
        for row in range(n - 1, -1, -1):
            for col in columns:
                cells[label] = (row, col)
                label += 1
            columns.reverse()

        # record steps to reach each cell
        dis = [-1] * (n ** 2 + 1)
        dis[1] = 0
        q = deque([1])
        while q:
            curr = q.popleft()
            for nxt in range(curr + 1, min(curr + 6, n * n) + 1):
                row, col = cells[nxt]
                dest = (board[row][col] if board[row][col] != -1 else nxt)
                # if not visited
                if dis[dest] == -1:
                    dis[dest] = dis[curr] + 1
                    q.append(dest)
        return dis[n ** 2]

