#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/9/29
"""
# You are given an integer array coins representing coins of different denominations
# and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.
# coins = [1,2,5], amount = 11
# 3


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # initialize a list with inf, hold the number of coins required for every amount from 0..amount
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i-c] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1