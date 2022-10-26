# Given an integer array nums and an integer k,
# return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k,
# or false otherwise.
#
# An integer x is a multiple of k if there exists an integer n such that x = n * k.
# 0 is always a multiple of k.


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {0: -1}
        totalSum = 0
        for i, v in enumerate(nums):
            totalSum += v
            curr = totalSum % k
            if curr in d:
                if i - d.get(curr) > 1:
                    return True
            else:
                d[curr] = i
        return False
