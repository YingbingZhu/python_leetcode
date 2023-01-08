#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/10/13
"""
# Given four integers sx, sy, tx, and ty,
# return true if it is possible to convert the point (sx, sy) to the point (tx, ty) through some operations,
# or false otherwise.
#
# The allowed operation on some point (x, y) is to convert it to either (x, x + y) or (x + y, y).


class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while tx > sx and ty > sy:
            tx, ty = tx % ty, ty % tx
        return sx == tx and sy <= ty and (ty - sy) % sx == 0 or sy == ty and sx <= tx and (tx - sx) % sy == 0
