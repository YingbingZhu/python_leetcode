#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/20
"""
# You are given an array of integers nums and an integer target.
#
# Return the number of non-empty subsequences of nums such
# that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large,
# return it modulo 109 + 7.


class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        mod = 10**9 + 7
        nums.sort()
        l = 0
        r = len(nums) - 1
        while l <= r:
            curr = nums[l] + nums[r]
            if curr > target:
                r -= 1
            else:
                count += pow(2, r - l, mod)
                l += 1
        return count % mod


