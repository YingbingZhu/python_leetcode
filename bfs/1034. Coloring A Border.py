#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/10/13
"""
# You are given an m x n integer matrix grid, and three integers row, col, and color.
# Each value in the grid represents the color of the grid square at that location.
#
# Two squares belong to the same connected component
# if they have the same color and are next to each other in any of the 4 directions.
#
# The border of a connected component is all the squares in the connected component
# that are either 4-directionally adjacent to a square not in the component,
# or on the boundary of the grid (the first or last row or column).
#
# You should color the border of the connected component that contains the square grid[row][col] with color.
#
# Return the final grid.
from collections import deque


class Solution(object):
    def colorBorder(self, grid, row, col, color):
        """
        :type grid: List[List[int]]
        :type row: int
        :type col: int
        :type color: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        q = deque([(row, col)])

        visited = set()
        visited.add((row, col))

        border = set()

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for rr, cc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                    if 0 <= rr < m and 0 <= cc < n and grid[rr][cc] == grid[r][c]:
                        if (rr, cc) not in visited:
                            q.append((rr, cc))
                            visited.add((rr, cc))
                    else:
                        border.add((r,c))
        for x, y in border:
            grid[x][y] = color
        return grid
