#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/23
"""


class Solution(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        while n > 1:
            newNums = [0] * (n//2)
            for i in range(n//2):
                if i % 2 == 0:
                    newNums[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    newNums[i] = max(nums[2 * i], nums[2 * i + 1])
            nums = newNums
            n = len(nums)
        return nums[0]
