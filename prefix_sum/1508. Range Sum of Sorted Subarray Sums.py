#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/21
"""
import heapq


class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        # temp = []
        # for i in range(len(nums)):
        #     prefix = nums[i]
        #     temp.append(prefix)
        #     for j in range(i+1, len(nums)):
        #         prefix += nums[j]
        #         temp.append(prefix)
        # temp.sort()
        # print(temp)
        # return sum(temp[left-1:right]) % (10**9 + 7)
        h = [(x, i) for i, x in enumerate(nums)]
        print(h)
        heapq.heapify(h)

        for k in range(1, right+1):
            x, i = heapq.heappop(h)
            if k



if __name__ == "__main__":
    s = Solution()
    s.rangeSum(nums = [1,2,3,4], n = 4, left = 1, right = 5)