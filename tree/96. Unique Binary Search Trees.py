#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/16
"""
# Given an integer n,
# return the number of structurally unique BST's (binary search trees) '
# which has exactly n nodes of unique values from 1 to n.


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]

        # catalan number : factorial(2*n) // (factorial(n)*factorial(n+1))
