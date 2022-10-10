#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/10/8
"""
# Given an array nums with n objects colored red, white, or blue,
# sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#
# You must solve this problem without using the library's sort function.
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """