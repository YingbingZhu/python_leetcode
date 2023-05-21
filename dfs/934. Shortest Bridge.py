class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()
        # find first island
        def dfs(i, j):
            if grid[i][j] == 1:
                q.append((i, j, 0))
                grid[i][j] = '$'
                if i - 1 >= 0:
                    dfs(i-1, j)
                if i + 1 < len(grid):
                    dfs(i+1, j)
                if j - 1 >= 0:
                    dfs(i, j - 1)
                if j + 1 < len(grid):
                    dfs(i, j + 1)
        
        # expand 
        def bfs(q):
            seen = set()
            while q:
                i, j, d = q.popleft()
                # find the other island
                if grid[i][j] == 1:
                    return d
                else:
                    for ii, jj in ((i-1, j), (i, j-1), (i+1, j), (i, j+1)):
                        if 0 <= ii < len(grid) and 0 <= jj < len(grid):
                            if (ii, jj) not in seen:
                                seen.add((ii, jj))
                                q.append((ii, jj, d + 1))
        flag = False
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1:
                    dfs(i, j)
                    flag = True
                    break
            if flag:
                break
        
        return bfs(q) - 1
        

            
            