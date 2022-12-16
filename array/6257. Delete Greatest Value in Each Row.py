class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for row in grid:
            row.sort()
        res = 0
        for row in zip(*grid):
            res += max(row)
        print(res)
        return res


if __name__ == "__main__":
    s = Solution()
    grid = [[1,2,4],[3,3,1]]
    s.deleteGreatestValue(grid)