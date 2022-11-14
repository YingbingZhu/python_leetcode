#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/11
"""
# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
#
# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice,
# and the combinations may be returned in any order.


class Solution(object):
    def __init__(self):
        self.res = []

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.backtrack(1, n, k, [])
        print(self.res)
        return self.res

    def backtrack(self, index, n, k, comb):
        if n < 0:
            return
        if n == 0 and k == 0:
            self.res.append(comb)
            return
        for i in range(index, 10):
            self.backtrack(i+1, n-i, k-1, comb + [i])


if __name__ == "__main__":
    s = Solution()
    s.combinationSum3(3, 9)


