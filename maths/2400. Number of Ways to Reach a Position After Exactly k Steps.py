#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/10/13
"""
# You are given two positive integers startPos and endPos. Initially,
# you are standing at position startPos on an infinite number line. With one step,
# you can move either one position to the left, or one position to the right.
#
# Given a positive integer k, return the number of different ways to reach the position endPos starting from startPos,
# such that you perform exactly k steps. Since the answer may be very large, return it modulo 109 + 7.
#
# Two ways are considered different if the order of the steps made is not exactly the same.
#
# Note that the number line includes negative integers.
from maths import comb


class Solution(object):
    def numberOfWays(self, startPos, endPos, k):
        """
        :type startPos: int
        :type endPos: int
        :type k: int
        :rtype: int
        """
        dist = abs(endPos - startPos)
        if (k - dist)//2 < 0 or k % 2 != dist % 2:
            return 0
        mod = 10**9 + 7
        # right = (b - a + k) / 2.
        # The combinations is to pick right steps from k steps to go right.
        return comb(k, (k - dist)//2) % mod

