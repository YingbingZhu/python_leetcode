#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/7
"""
# There is a rectangular brick wall in front of you with n rows of bricks.
# The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths.
# The total width of each row is the same.
#
# Draw a vertical line from the top to the bottom and cross the least bricks.
# If your line goes through the edge of a brick, then the brick is not considered as crossed.
# You cannot draw a line just along one of the two vertical edges of the wall,
# in which case the line will obviously cross no bricks.
#
# Given the 2D array wall that contains the information about the wall,
# return the minimum number of crossed bricks after drawing such a vertical line.


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        cracks = {0: 0}
        for row in wall:
            x = 0
            for brick in row[:-1]:
                x += brick
                cracks[x] = cracks.get(x, 0) + 1
        print(cracks)
        return len(wall) - max(cracks.values())


if __name__ == "__main__":
    s = Solution()
    wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
    s.leastBricks(wall)