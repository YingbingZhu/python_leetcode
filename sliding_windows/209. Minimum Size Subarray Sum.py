#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/27
"""


# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums) + 1
        left = 0
        total = 0
        for right, v in enumerate(nums):
            total += v
            while total >= target:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
        return res if res <= len(nums) else 0



if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    Solution().minSubArrayLen(target, nums)
