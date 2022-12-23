#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/23
"""
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_max = right_max = 0
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    res += left_max - height[l]
                l += 1
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    res += right_max - height[r]
                r -= 1
        return res



