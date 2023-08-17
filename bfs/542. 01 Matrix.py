class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        seen = set()
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    seen.add((i, j))
        

        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dis = 1
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for d in dir:
                    ii, jj = i + d[0], j + d[1]
                    if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in seen:
                        q.append((ii, jj))
                        seen.add((ii, jj))
                        mat[ii][jj] = dis
            dis += 1
        
        return mat
                        
            