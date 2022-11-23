#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/23
"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # validate row
        rows = len(board)
        cols = len(board[0])
        print(board)
        print(list(zip(*board)))

        for i in range(9):
            row = board[i]
            curr = set()
            for digit in row:
                if digit in curr:
                    return False
                elif digit != '.':
                    curr.add(digit)

        board = list(zip(*board))
        for i in range(9):
            row = board[i]
            curr = set()
            for digit in row:
                if digit in curr:
                    return False
                elif digit != '.':
                    curr.add(digit)

        # find the up-left cell
        for k in range(0, 9, 3):
            for i in range(0, 9, 3):
                curr = set()
                for x in range(i, i+3):
                    for y in range(k, k+3):
                        cell = board[x][y]
                        print(x, y)
                        if cell in curr:
                            return False
                        elif cell != '.':
                            curr.add(cell)
        print(1)
        return True


if __name__ == "__main__":
    board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    s = Solution()
    s.isValidSudoku(board)

