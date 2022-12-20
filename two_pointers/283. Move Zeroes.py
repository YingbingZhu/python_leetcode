#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/19
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[p] = nums[i]
                p += 1
        for i in range(p, len(nums)):
            nums[i] = 0




