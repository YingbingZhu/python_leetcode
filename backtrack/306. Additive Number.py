#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/10
"""
# An additive number is a string whose digits can form an additive sequence.
#
# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.
#
# Given a string containing only digits, return true if it is an additive number or false otherwise.
#
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
# Input: "112358"
# Output: true
# Explanation:
# The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in range(1, n//2 + 1):
            for j in range(1, (n - i)//2 + 1):
                if not self.isValid(num[:i], num[i:i+j], num[i+j:]):
                    return False
        return True

    def isValid(self, first, second, s):
        if (first[0] == '0' and len(first) > 1) or (second[0] == '0' and len(second) > 1):
            return False
        curr = str(int(first) + int(second))
        if curr == s:
            return True
        elif s.startswith(curr):
            return self.isValid(second, curr, s[len(curr):])
        else:
            return False



