#!/usr/bin/env python
"""
 Created by ZhuYB at 2023/1/6
"""

class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        res = 0
        i = 0
        while i < len(costs) and coins > 0:
            coins -= costs[i]
            if coins >= 0:
                res += 1
            i += 1
        return res