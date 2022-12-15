#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/15
"""

# Given an unsorted integer array nums, return the smallest missing positive integer.
#
# You must implement an algorithm that runs in O(n) time and uses constant extra space.


class Solution(object):
    def firstMissingPositive(self, nums):
        """

        :type nums: List[int]
        :rtype: int
        """
        missing = 1
        for num in nums:
            if num > 1 and num < missing:
                missing = num - 1
            if num == missing:
                missing += 1
            print(missing)
        return missing


if __name__ == "__main__":
    nums = [2,1]
    Solution().firstMissingPositive(nums)
