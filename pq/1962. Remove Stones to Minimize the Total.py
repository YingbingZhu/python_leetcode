#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/28
"""
import heapq
from math import floor


# You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile,
# and an integer k. You should apply the following operation exactly k times:
#
# Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
# Notice that you can apply the operation on the same pile more than once.
#
# Return the minimum possible total number of stones remaining after applying the k operations.
#
# floor(x) is the greatest integer that is smaller than or equal to x (i.e., rounds x down).


class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        rpiles = [-p for p in piles]
        heapq.heapify(rpiles)
        while k > 0:
            element = heapq.heappop(rpiles)
            heapq.heappush(rpiles, -(-element - (-element)//2))
            k -= 1
        res = 0
        print(rpiles)
        for p in rpiles:
            if p < 0:
                res += -p
            else:
                res += p
        print(res)
        return res


if __name__ == '__main__':
    piles = [1]
    k = 10000
    Solution().minStoneSum(piles, k)
