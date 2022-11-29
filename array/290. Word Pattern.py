#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/29
"""


class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        d = {}
        sl = s.split(' ')
        if len(pattern) != len(sl) or len(set(sl)) != len(set(pattern)):
            return False
        for i in range(len(pattern)):
            p = pattern[i]
            if p not in d:
                d[p] = sl[i]
            else:
                if d[p] != sl[i]:
                    return False
        return True
