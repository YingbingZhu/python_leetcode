#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/23
"""


class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """

        def helper(n, left):
            if n == 1:
                return 1
            if left:
                return 2 * helper(n//2, False)
            # from right
            if n % 2 == 1:
                return 2 * helper(n//2, True)
            else:
                return 2 * helper(n//2, True) - 1

        return helper(n, True)



