class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        def dfs(rr, cc):
            if rr < 0 or rr >= m or cc < 0 or cc >= n:
                return 0
            if grid[rr][cc]:
                return 1
            #  mark 0 as visited
            grid[rr][cc] = 2
            return dfs(rr, cc+1) * dfs(rr-1, cc) * dfs(rr, cc-1) * dfs(rr+1, cc)
        
        return sum(dfs(i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == 0)
