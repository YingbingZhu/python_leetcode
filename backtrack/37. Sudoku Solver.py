#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/10
"""

# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def isValid(r, c, ch):
            r = int(r)
            c = int(c)

            for i in range(9):
                if board[i][c] == ch or board[r][i] == ch:
                    return False
                if board[3 * (r//3) + i//3][3 * (c//3) + i%3] == ch:
                    return False
            return True

        # start at row 0, solve every column
        def solve(r, c):
            if r == 9:
                return True
            if c == 9:
                return solve(r+1, 0)

            if board[r][c] == '.':
                for i in range(1, 10):
                    if isValid(r, c, str(i)):
                        board[r][c] = str(i)
                        if solve(r, c+1):
                            return True
                        else:
                            # undo
                            board[r][c] = '.'
                return False
            else:
                return solve(r, c+1)

        solve(0, 0)










