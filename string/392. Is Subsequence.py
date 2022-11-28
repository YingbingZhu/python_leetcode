#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/28
"""
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting
# some (can be none) of the characters without disturbing the relative positions of the remaining characters.
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ps = pt = 0
        while ps < len(s) and pt < len(t):
            if s[ps] == t[pt]:
                ps += 1
            pt += 1
        print(ps)
        return ps == len(s)


if __name__ == "__main__":
    s1 = Solution()
    s = "abc"
    t = "ahbgdc"
    s1.isSubsequence(s, t)


