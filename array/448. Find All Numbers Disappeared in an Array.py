#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/29
"""


# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = set(i for i in range(1, len(nums)+1))
        print(res)
        for num in nums:
            if num in res:
                res.remove(num)
        return list(res)


if __name__ == "__main__":
    s = Solution()
    nums = [1,1]
    s.findDisappearedNumbers(nums)
