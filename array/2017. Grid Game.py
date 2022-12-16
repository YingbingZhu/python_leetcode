class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        suffix = [num for num in grid[0]]
        suf = 0
        for i in range(len(suffix) - 1, -1, -1):
            suffix[i] = suf
            suf += grid[0][i]

        prefix = [num for num in grid[1]]
        pre = 0
        for i in range(len(prefix)):
            prefix[i] = pre
            pre += grid[1][i]

        # player 1 minimize, player 2 maximize
        res = float('inf')
        for i in range(len(grid[0])):
            res = min(res, max(prefix[i], suffix[i]))

        return res
