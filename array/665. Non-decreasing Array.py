#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/14
"""


# Given an array nums with n integers, your task is to check if
# it could become non-decreasing by modifying at most one element.
#
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based)
# such that (0 <= i <= n - 2).


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return True
        count = int(nums[0] > nums[1])
        for i in range(2, len(nums)):
            if nums[i] < nums[i - 1]:
                if count > 0:
                    return False
                count += 1
                if nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i - 2]
                else:
                    nums[i] = nums[i - 1]
                print(nums)
        return True


if __name__ == "__main__":
    Solution().checkPossibility(nums=[1,4,1,2])