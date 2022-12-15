#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/14
"""


# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money
# you can rob tonight without alerting the police.


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        dp[2] = max(dp[1], dp[0] + nums[2])
        for i in range(3, len(dp)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]


if __name__ == "__main__":
    Solution().rob(nums=[2, 7, 9, 3, 1])
