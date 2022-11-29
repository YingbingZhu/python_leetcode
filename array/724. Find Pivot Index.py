#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/29
"""


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        S = sum(nums)
        pre = 0
        for i in range(len(nums)):
            if pre == (S - nums[i] - pre):
                return i
            pre += nums[i]
        return -1


if __name__ == "__main__":
    s = Solution()
    s.pivotIndex(nums=[1, 7, 3, 6, 5, 6])
