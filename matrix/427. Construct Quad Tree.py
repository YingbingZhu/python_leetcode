"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        grid_sum = sum([sum(row) for row in grid])
        n = len(grid)
        # base case
        if grid_sum == 0 or grid_sum == n * n:
            return Node(grid_sum // (n * n), True, None, None, None, None)

        topml = [i[:n // 2] for i in grid[:n // 2]]
        topmr = [i[n // 2:] for i in grid[:n // 2]]
        botml = [i[:n // 2] for i in grid[n // 2:]]
        botmr = [i[n // 2:] for i in grid[n // 2:]]

        tl = self.construct(topml)
        tr = self.construct(topmr)
        bl = self.construct(botml)
        br = self.construct(botmr)

        return Node(1, False, tl, tr, bl, br)
