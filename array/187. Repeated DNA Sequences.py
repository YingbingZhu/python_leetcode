#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/15
"""
# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
#
# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.
#
# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings)
# that occur more than once in a DNA molecule. You may return the answer in any order.


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        res = []
        for i in range(len(s)-9):
            l = i
            r = i + 9
            sub = s[l:r+1]
            if sub in seen and sub not in res:
                res.append(sub)
            seen.add(sub)
        return res