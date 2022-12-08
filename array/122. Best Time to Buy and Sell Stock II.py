#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/7
"""
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
#
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
# However, you can buy it then immediately sell it on the same day.
#
# Find and return the maximum profit you can achieve.


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(prices) - 1):
            res += max(0, prices[i + 1] - prices[i])
        return res



if __name__ == "__main__":
    s = Solution()
    prices = [7,1,5,3,6,4]
    s.maxProfit(prices)
