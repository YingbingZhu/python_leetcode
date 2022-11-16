#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/16
"""


class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        arr = [first]
        for i in range(len(encoded)):
            arr.append(encoded[i] ^ arr[i])
        return arr