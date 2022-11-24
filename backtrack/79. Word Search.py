#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/24
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def backtrack(i, j, index, visited):
            if board[i][j] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            visited.add((i, j))
            for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ii < len(board) and 0 <= jj < len(board[0]) and (ii, jj) not in visited:
                    if backtrack(ii, jj, index + 1, visited):
                        return True
            visited.remove((i, j))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0, set()):
                    return True

        return False