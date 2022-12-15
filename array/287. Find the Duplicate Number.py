#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/15
"""
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
#
# There is only one repeated number in nums, return this repeated number.
#
# You must solve the problem without modifying the array nums and uses only constant extra space.


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count the
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            count = sum(num <= mid for num in nums)
            if count > mid:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

