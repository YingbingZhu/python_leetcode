#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/23
"""
# You are given a 0-indexed array nums of distinct integers.
# You want to rearrange the elements in the array such that every element in the rearranged array
# is not equal to the average of its neighbors.
#
# More formally, the rearranged array should have the property
# such that for every i in the range 1 <= i < nums.length - 1,
# (nums[i-1] + nums[i+1]) / 2 is not equal to nums[i].
#
# Return any rearrangement of nums that meets the requirements.


class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # make array wave
        nums.sort()
        for i in range(1, len(nums), 2):
            nums[i], nums[i-1] = nums[i-1], nums[i]
        return nums


