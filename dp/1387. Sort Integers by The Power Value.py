#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/7
"""


# if x is even then x = x / 2
# if x is odd then x = 3 * x + 1
# Input: lo = 12, hi = 15, k = 2
# Output: 13
# Explanation: The power of 12 is 9 (12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1)
# The power of 13 is 9
# The power of 14 is 17
# The power of 15 is 17
# The interval sorted by the power value [12,13,14,15]. For k = 2 answer is the second element which is 13.
# Notice that 12 and 13 have the same power value and we sorted them in ascending order.
# Same for 14 and 15.


class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        cache = {1: 1}

        def power(n):
            if n not in cache:
                if n % 2 == 0:
                    cache[n] = 1 + power(n // 2)
                else:
                    cache[n] = 1 + power(3 * n + 1)
            return cache[n]

        return sorted((power(i), i) for i in range(lo, hi + 1))[k - 1][1]
