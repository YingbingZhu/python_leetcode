#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/9/30
"""

# You are given an m x n grid where each cell can have one of three values:
#
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.
# If this is impossible, return -1.
from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        queue = deque()

        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        minute = 0
        while queue and fresh:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for (rr, cc) in [(r-1, c), (r, c-1), (r+1, c), (r, c+1)]:
                    if 0 <= rr < m and 0 <= cc < n and grid[rr][cc] == 1:
                        queue.append((rr, cc))
                        grid[rr][cc] = 2
                        fresh -= 1
            minute += 1

        return minute if fresh == 0 else -1


