#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/10/24
"""
# You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr
# that has unique characters.
#
# Return the maximum possible length of s.
#
# A subsequence is an array that can be derived from another array by deleting some
# or no elements without changing the order of the remaining elements.


class Solution(object):
    def __init__(self):
        self.length = 0

    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        self.backtrack(arr, 0, "")
        return self.length

    def backtrack(self, arr, index, comb):
        if len(comb) != len(set(comb)):
            return
        self.length = max(len(comb), self.length)
        for i in range(index, len(arr)):
            self.backtrack(arr, i+1, comb+arr[i])





