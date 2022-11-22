#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/21
"""
from collections import deque


class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        rows = len(maze)
        cols = len(maze[0])

        queue = deque()
        queue.append((entrance[0], entrance[1], 0))
        while queue:
            r, c, steps = queue.popleft()
            # if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and (r != entrance[0] and c != entrance[1]):
            #     print(steps)
            #     return steps
            for rr, cc in [(r-1, c), (r, c-1), (r+1, c), (r, c+1)]:
                if 0 <= rr < rows and 0 <= cc < cols and maze[rr][cc] != '+':
                    maze[rr][cc] = '+'
                    queue.append((rr, cc, steps+1))
                    if (rr == 0 or rr == rows - 1 or cc == 0 or cc == cols - 1) and (not (rr == entrance[0] and cc == entrance[1])):
                        print(steps+1)
                        return steps+1

        return -1




if __name__ == "__main__":
    s = Solution()
    maze = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".","+",".","+"],["+","+","+","+","+",".","+"]]
    entrance = [0,1]
    s.nearestExit(maze, entrance)
