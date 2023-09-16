#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/9/30
"""
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
# return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set()
        stack = []
        num = 0

        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    visited.add((i, j))
                    stack.append((i, j))

                    while stack:
                        r, c = stack.pop()

                        for rr, cc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                            if 0 <= rr < m and 0 <= cc < n and (rr, cc) not in visited and grid[rr][cc] == "1":
                                stack.append((rr, cc))
                                visited.add((rr, cc))
                    num += 1
        return num

# solution 2: using dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j >= len(grid[0]) or j < 0 or grid[i][j] != '1':
                return
            grid[i][j] = '#'
            for (ii, jj) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                dfs(ii, jj)s
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    cnt += 1

        return cnt

