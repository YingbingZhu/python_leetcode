#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/26
"""
from collections import Counter


# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        target = [0] * 26
        window = [0] * 26
        for s in s1:
            target[ord(s) - ord('a')] += 1

        length = len(s1)
        for i, s in enumerate(s2):
            print(window)
            window[ord(s) - ord('a')] += 1
            if i >= length:
                window[ord(s2[i-length]) - ord('a')] -= 1
            if window == target:
                return True
        return False



if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    Solution().checkInclusion(s1, s2)