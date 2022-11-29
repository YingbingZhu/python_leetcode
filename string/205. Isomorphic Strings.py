#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/28
"""


# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_t = {}
        t_s = {}
        for i in range(len(s)):
            if s[i] not in s_t and t[i] not in t_s:
                s_t[s[i]] = t[i]
                t_s[t[i]] = s[i]
                print(s_t)
                print(t_s)
            elif s[i] in s_t and s_t[s[i]] != t[i]:
                return False
            elif t[i] in t_s and t_s[t[i]] != s[i]:
                return False
        return True


if __name__ == "__main__":
    S = Solution()
    s = "paper"
    t = "title"
    S.isIsomorphic(s, t)
