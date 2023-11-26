class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        for i in range(1, n):
            for j in range(m):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
        
        ans = 0
        for i in range(n):
            matrix[i].sort()
            for j in range(m):
                ans = max(ans, matrix[i][j] * (m - j))

        return ans
