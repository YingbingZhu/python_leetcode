#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/10/8
"""

# Given two strings s and t of lengths m and n respectively,
# return the minimum window substring of s such that
# every character in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".
#
# The testcases will be generated such that the answer is unique.
#
# A substring is a contiguous sequence of characters within the string.

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_count = Counter(t)
        required = len(t_count)
        l = r = 0
        min_win = len(s) + 1
        res_l = 0
        while r < len(s):
            character = s[r]
            if character in t_count:
                # if this char is a "must_have"
                if t_count[character] > 0:
                    required -= 1
                t_count[character] -= 1

            # find a smaller window
            while required == 0:
                if r - l + 1 < min_win:
                    min_win = r - l + 1
                    res_l = l

                if s[l] in t_count:
                    t_count[s[l]] += 1

                    if t_count[s[l]] > 0:
                        required += 1

                l += 1

            # move right pointer to include all required chars
            r += 1

        if min_win == len(s) + 1:
            return ""
        else:
            # current r is not optimal
            return s[res_l: res_l + min_win]



