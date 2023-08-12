class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        @cache
        def dfs(i, j):
            if obstacleGrid[i][j] == 1:
                return 0
            if i == m-1 and j == n-1:
                return 1
            count = 0
            if i < m -1:
                count += dfs(i+1, j)
            if j < n - 1:
                count += dfs(i, j+1)
            return count

        return dfs(0, 0)
