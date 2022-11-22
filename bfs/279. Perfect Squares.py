#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/22
"""
from collections import deque


# Given an integer n, return the least number of perfect square numbers that sum to n.
#
# A perfect square is an integer that is the square of an integer; in other words,
# it is the product of some integer with itself.
#     For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        sqs = {i * i for i in range(1, n//2+1) if i * i <= n}
        queue = deque([(n, 0)])
        seen = set()
        seen.add(n)
        while queue:
            curr, depth = queue.popleft()
            if curr == 0:
                return depth
            for sq in sqs:
                if curr - sq >= 0 and curr - sq not in seen:
                    seen.add(curr - sq)
                    queue.append((curr - sq, depth + 1))

        return n



