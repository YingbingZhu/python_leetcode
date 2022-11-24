#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/24
"""


class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        n = len(matrix)

        for i in range(n):
            row = matrix[i]
            if len(row) != len(set(row)) or min(row) != 1 or max(row) != n:
                return False

        for i in range(n):
            col = list(zip(*matrix))[i]
            if len(col) != len(set(col)) or min(col) != 1 or max(col) != n:
                return False

        return True
