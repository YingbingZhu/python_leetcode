#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/10
"""
# The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.
#
# For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
# Given an array nums, return the sum of all XOR totals for every subset of nums.
#
# Note: Subsets with the same elements should be counted multiple times.
#
# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

# Input: nums = [1,3]
# Output: 6
# Explanation: The 4 subsets of [1,3] are:
# - The empty subset has an XOR total of 0.
# - [1] has an XOR total of 1.
# - [3] has an XOR total of 3.
# - [1,3] has an XOR total of 1 XOR 3 = 2.
# 0 + 1 + 3 + 2 = 6


class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = 0

        def dfs(index, current):
            nonlocal res
            if index == n:
                res += current
                return
            # include current num
            dfs(index+1, current ^ nums[index])
            # not include current num
            dfs(index+1, current)

        dfs(0, 0)
        return res


if __name__ == "__main__":
    s = Solution()
    s.subsetXORSum([1, 3])