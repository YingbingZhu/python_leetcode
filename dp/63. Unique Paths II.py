class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        prev = [0 for _ in range(n)]
        prev[0] = 1
        cur = [0 for _ in range(n)]

        for i in range(m):
            cur[0] = 0 if obstacleGrid[i][0] == 1 else prev[0]
            for j in range(1, n):
                cur[j] = 0 if obstacleGrid[i][j] == 1 else prev[j] + cur[j - 1]
            prev = cur

        return prev[-1]

        return dp[-1][-1]
