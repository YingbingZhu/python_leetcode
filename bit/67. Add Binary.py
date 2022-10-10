#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/10/8
"""
# Given two binary strings a and b, return their sum as a binary string.
# Input: a = "1010", b = "1011"
# Output: "10101"


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a) - 1, len(b) - 1
        res = ""
        carry = 0
        while i >= 0 or j >= 0:
            digit = carry
            if i >= 0:
                digit += ord(a[i]) - ord('0')
            if j >= 0:
                digit += ord(b[j]) - ord('0')
            i -= 1
            j -= 1
            carry = 1 if digit > 1 else 0
            res += str(digit % 2)

        if carry != 0:
            res += str(carry)

        return res[::-1]

