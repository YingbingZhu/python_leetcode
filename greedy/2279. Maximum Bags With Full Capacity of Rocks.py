#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/27
"""


# You have n bags numbered from 0 to n - 1. You are given two 0-indexed integer arrays capacity and rocks.
# The ith bag can hold a maximum of capacity[i] rocks and currently contains rocks[i] rocks.
# You are also given an integer additionalRocks, the number of additional rocks you can place in any of the bags.
#
# Return the maximum number of bags that could have full capacity after placing the additional rocks in some bags.


class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        diff = []
        n = len(rocks)
        for i in range(n):
            diff.append(capacity[i] - rocks[i])

        diff.sort()
        count = 0
        for d in diff:
            if additionalRocks < d:
                break
            else:
                additionalRocks -= d
                count += 1

        return count


if __name__ == '__main__':
    capacity = [91, 54, 63, 99, 24, 45, 78]
    rocks = [35, 32, 45, 98, 6, 1, 25]
    additionalRocks = 17
    Solution().maximumBags(capacity, rocks, additionalRocks)
