#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/2
"""
# Given an integer n, return the number of structurally unique BST
# which has exactly n nodes of unique values from 1 to n.


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * n
        for i in range(1, n):
            dp[i] = dp[i-1]
