#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/16
"""
# An n-bit gray code sequence is a sequence of 2n integers where:
#
# Every integer is in the inclusive range [0, 2n - 1],
# The first integer is 0,
# An integer appears no more than once in the sequence,
# The binary representation of every pair of adjacent integers differs by exactly one bit, and
# The binary representation of the first and last integers differs by exactly one bit.
# Given an integer n, return any valid n-bit gray code sequence.
# pattern
# [00, 01, 11, 10]
# [000, 001, 011, 010, 110, 111, 101, 100]


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0]
        for i in range(n):
            ans += [(1 << i) ^ num for num in ans[::-1]]
        return ans

