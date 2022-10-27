# You are given a 0-indexed integer array nums of length n.
#
# The average difference of the index i is the absolute difference between the average of the first i + 1 elements of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.
#
# Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.
#
# Note:
#
# The absolute difference of two numbers is the absolute value of their difference.
# The average of n elements is the sum of the n elements divided (integer division) by n.
# The average of 0 elements is considered to be 0.


class Solution(object):
    def minimumAverageDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            pre[i + 1] = pre[i] + nums[i]
        suf = [0] * (len(nums) + 1)
        for i in range(len(nums) - 1, -1, -1):
            suf[i] = suf[i + 1] + nums[i]

        res = -1
        minVal = float('inf')
        for i in range(len(nums)):
            left = pre[i + 1] // (i + 1)
            right = suf[i + 1]
            if i != len(nums) - 1:
                right = suf[i + 1] // (len(nums) - i - 1)
            curr = abs(left - right)
            if curr < minVal:
                minVal = curr
                res = i
        return res
