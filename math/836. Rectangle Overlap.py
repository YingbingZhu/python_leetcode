#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/17
"""


class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        if rec1[0] >= rec2[2] or rec1[1] >= rec2[4] or rec2[0] >= rec1[2] or rec2[1] >= rec1[4]:
            return False
        return True