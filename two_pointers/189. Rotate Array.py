#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/23
"""


# Given an array, rotate the array to the right by k steps, where k is non-negative.
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        n = len(nums) - 1
        k %= len(nums)
        # reverse whole
        reverse(0, n)
        reverse(0, k-1)
        reverse(k, n)
        print(k)
        print(nums)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    Solution().rotate(nums, k)
