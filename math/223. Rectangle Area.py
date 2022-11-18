#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/17
"""


class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        area1 = (ay2 - ay1) * (ax2 - ax1)
        area2 = (by2 - by1) * (bx2 - bx1)
        if ax1 >= bx2 or ay1 >= by2 or bx1 >= ax2 or by1 >= ay2:
            return area1 + area2

        delta_x = min(ax2, bx2) - max(ax1, bx1)
        delta_y = min(ay2, by2) - max(ay1, by1)
        print(delta_x)
        print(delta_y)
        print(area1 + area2)
        return area1 + area2 - delta_x * delta_y


if __name__ == "__main__":
    s = Solution()
    s.computeArea(ax1=-3, ay1=0, ax2=3, ay2=4, bx1=0, by1=-1, bx2=9, by2=2)
