#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/10/14
"""
# Winter is coming! During the contest, your first job is to design a standard heater
# with a fixed warm radius to warm all the houses.
#
# Every house can be warmed, as long as the house is within the heater's warm radius range.
#
# Given the positions of houses and heaters on a horizontal line,
# return the minimum radius standard of heaters so that those heaters could cover all houses.
#
# Notice that all the heaters follow your radius standard, and the warm radius will the same.


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        houses.sort()
        radius = 0
        # index of closet heater in the left
        i = 0
        for house in houses:
            while i + 1 < len(heaters) and heaters[i+1] < house:
                i += 1
            # min distance of left and right
            minDist = min([abs(house - heater) for heater in heaters[i:i+2]])
            radius = max(minDist, radius)
        return radius