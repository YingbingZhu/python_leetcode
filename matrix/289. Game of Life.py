class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        dirs = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
        for i in range(m):
            for j in range(n):
                lives = 0
                for d in dirs:
                    ii = i + d[0]
                    jj = j + d[1]
                    if 0 <= ii < m and 0 <= jj < n and abs(board[ii][jj]) == 1:
                        lives += 1
                if board[i][j] == 1:
                    if lives < 2 or lives > 3:
                        board[i][j] = -1
                else:
                    if lives == 3:
                        board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0

