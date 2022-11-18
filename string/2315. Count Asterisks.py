#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/17
"""
# You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair.
# In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.
#
# Return the number of '*' in s, excluding the '*' between each pair of '|'.
#
# Note that each '|' will belong to exactly one pair.


class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        pair = 0
        for c in s:
            if pair == 0:
                if c == '*':
                    ans += 1
                if c == '|':
                    pair = 1
            elif c == '|':
                pair = 0
        return ans
