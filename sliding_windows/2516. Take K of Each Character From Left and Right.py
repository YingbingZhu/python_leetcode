#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/28
"""
from collections import Counter


# You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute,
# you may take either the leftmost character of s, or the rightmost character of s.
#
# Return the minimum number of minutes needed for you to take at least k of each character,
# or return -1 if it is not possible to take k of each character.


class Solution(object):
    def takeCharacters(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        counter = Counter(s)
        required = {}