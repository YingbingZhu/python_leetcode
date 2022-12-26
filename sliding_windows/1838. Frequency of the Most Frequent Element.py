#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/26
"""
# The frequency of an element is the number of times it occurs in an array.
#
# You are given an integer array nums and an integer k.
# In one operation, you can choose an index of nums and increment the element at that index by 1.
#
# Return the maximum possible frequency of an element after performing at most k operations.


class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        start = 0
        for end in range(len(nums)):
            k += nums[end]
            # move window
            if (end - start + 1) * nums[end] > k:
                k -= nums[start]
                start += 1
        return end - start + 1


if __name__ == '__main__':
    nums = [1, 2, 4]
    k = 5
    Solution().maxFrequency(nums, k)
