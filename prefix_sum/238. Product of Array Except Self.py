#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/9/30
"""
# Given an integer array nums,
# return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]

        # backwards
        tmp = 1
        for i in range(len(nums)-2, -1, -1):
            tmp *= nums[i+1]
            res[i] *= tmp

        return res


        # pre1 = []
        # curr = 1
        # for num in nums:
        #     curr *= num
        #     pre1.append(curr)
        #
        # pre2 = []
        # curr = 1
        # for num in nums[::-1]:
        #     curr *= num
        #     pre2.append(curr)
        #
        # res = [1] * len(nums)
        # res[0] = pre2[-2]
        # res[-1] = pre1[-2]
        # for i in range(1, len(nums)-1):
        #     res[i] = pre1[i-1] * pre2[len(nums)-i-2]

        return res


if __name__ == "__main__":
    nums = [-1, 1, 0, -3, 3]
    s = Solution()
    print(s.productExceptSelf(nums))

