#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/18
"""
# Given an integer array nums, your goal is to make all elements in nums equal.
# To complete one operation, follow these steps:
#
# Find the largest value in nums. Let its index be i (0-indexed) and its value be largest.
# If there are multiple elements with the largest value, pick the smallest i.
# Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
# Reduce nums[i] to nextLargest.
# Return the number of operations to make all elements in nums equal.


class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        i = 0
        ans = 0
        curr = 0
        while i < len(nums) - 1:
            if nums[i+1] < nums[i]:
                ans += curr
                curr = 0
            i += 1
        return ans