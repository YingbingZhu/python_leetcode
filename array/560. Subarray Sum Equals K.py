#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/7
"""
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
#
# A subarray is a contiguous non-empty sequence of elements within an array.


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        acc_sum = 0
        d = {0: 1}
        for num in nums:
            acc_sum += num
            # acc_sum - sum = k
            if acc_sum - k in d:
                res += d[acc_sum - k]
            d[acc_sum] = d.get(acc_sum, 0) + 1
        return res


if __name__ =="__main__":
    s = Solution()
    nums =[1,1,1]
    k = 3
    s.subarraySum(nums, k)



