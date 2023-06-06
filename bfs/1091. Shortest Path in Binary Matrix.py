class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        q = [(0, 0, 1)]
        grid[0][0] = 1
        for i, j, d in q:
            if i == n-1 and j == n-1: return d
            for ii, jj in [(i+1, j+1), (i-1, j-1), (i+1, j-1), (i-1, j+1), (i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= ii < n and 0 <= jj < n and not grid[ii][jj]:
                    grid[ii][jj] = 1
                    q.append((ii, jj, d+1))
        return -1
