#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/18
"""
# Given an array nums with n integers,
# your task is to check if it could become non-decreasing by modifying at most one element.
#
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if count == 1:
                    return False
                count += 1
                # greedy, compare with i - 2 and fix
                if i >= 2 and nums[i-2] > nums[i]:
                    nums[i] = nums[i-1]
        return True


if __name__ == "__main__":
    s = Solution()
    nums = [3,4,2,3]
    s.checkPossibility(nums)