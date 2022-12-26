#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/26
"""
# You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:
#
# Type-1: Remove the character at the start of the string s and append it to the end of the string.
# Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
# Return the minimum number of type-2 operations you need to perform such that s becomes alternating.
#
# The string is called alternating if no two adjacent characters are equal.
#
# For example, the strings "010" and "1010" are alternating, while the string "0100" is not.


class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        even = odd = 0
        for i, v in enumerate(s):
            if v == '1':
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1
        if len(s) % 2 == 0:
            return len(s) // 2 - max(even, odd)


