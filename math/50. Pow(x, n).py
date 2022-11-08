#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/4
"""
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
# Input: x = 2.10000, n = 3
# Output: 9.26100


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 1
        if n < 0:
            n = -n
            x = 1/x
        while n != 0:
            if (n & 1) != 0:  # n % 2 != 0
                res *= x
            x *= x
            n >>= 1  # n/2
        return res


if __name__ == "__main__":
    s = Solution()
    a = 8
    print(a >> 1)