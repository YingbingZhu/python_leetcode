#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/14
"""


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # islands * 4 - 2 * neighbors
        islands = 0
        neighbors = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    islands += 1
                    if j < len(grid[0]) - 1 and grid[i][j+1] == 1:
                        neighbors += 1
                    if i < len(grid) - 1 and grid[i+1][j] == 1:
                        neighbors += 1

        return islands * 4 - neighbors * 2



        # stack = []
        # visited = set()
        # n = len(grid)
        # m = len(grid[0])
        # for row in range(n):
        #     for col in range(m):
        #         if not stack and grid[row][col] == 1:
        #             stack.append((row, col))
        #             visited.add((row, col))
        #             break
        # print(stack)
        # ans = len(stack) * 4
        # while stack:
        #     r, c = stack.pop()
        #     for rr, cc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
        #         if 0 <= rr < n and 0 <= cc < m and grid[rr][cc] == 1 and (rr, cc) not in visited:
        #             ans += 2
        #             print(ans)
        #             stack.append((rr, cc))
        #             visited.add((rr, cc))
        # print(ans)
        # return ans


if __name__ == "__main__":
    s = Solution()
    grid = [[1,1],[1,1]]
    s.islandPerimeter(grid)