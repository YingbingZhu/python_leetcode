#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/20
"""


# You are given an integer array height of length n. There are n vertical lines drawn
# such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l = 0
        r = len(height) - 1
        lmax = height[l]
        rmax = height[r]
        while l < r:
            lmax = max(height[l], lmax)
            rmax = max(height[r], rmax)
            res = max(res, min(lmax, rmax) * (r - l))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        print(res)
        return res


if __name__ == "__main__":
    Solution().maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7])
