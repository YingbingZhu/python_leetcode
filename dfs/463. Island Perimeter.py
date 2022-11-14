#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/14
"""


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        stack = [(0, 0)]
        while stack:
            curr = stack.



if __name__ == "__main__":
    s = Solution()
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    s.islandPerimeter(grid)