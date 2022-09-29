#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/9/29
"""
# Given a sorted integer array arr, two integers k and x,
# return the k closest integers to x in the array. The result should also be sorted in ascending order.
#
# An integer a is closer to x than an integer b if:
#
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if k == len(arr):
            return arr
        # sliding window of length k
        l, r = 0, len(arr) - k
        while l < r:
            m = (l + r) // 2
            # x is closer to arr[m+k]
            if x - arr[m] > arr[m+k] - x:
                l = m + 1
            else:
                r = m
        return arr[l:l+k]