#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/12
"""


# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
#
# A good subarray is a subarray where:
#
# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:
#
# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
#
# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.


# (pre[r+1] - pre[l]) % k = 0
# pre[r+1] % k = pre[l] % k
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {0: 0}
        pre = 0
        for i in range(len(nums)):
            pre += nums[i]
            print(d)
            # d[pre % k]
            if pre % k in d and d[pre % k] < i:
                return True
            if pre % k not in d:
                d[pre % k] = i + 1
        return False


if __name__ == "__main__":
    nums = [5, 5, 0, 0]
    k = 3
    Solution().checkSubarraySum(nums, k)
