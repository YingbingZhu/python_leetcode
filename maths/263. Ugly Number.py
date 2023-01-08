#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/18
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        lst = [2, 3, 5]
        for num in lst:
            n = self.reduce(n, num)
        return n == 1

    def reduce(self, dividend, divisor):
        while dividend % divisor == 0:
            dividend //= divisor
        return dividend