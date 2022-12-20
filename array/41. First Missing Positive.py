#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/15
"""


# Given an unsorted integer array nums, return the smallest missing positive integer.
#
# You must implement an algorithm that runs in O(n) time and uses constant extra space.


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        must be in range: [1, len(nums)+1]

        So consider an array like [1,4,3,3,3]. The length is 5, so n = 5.
       overwriting the spot at the index of the item with 5 + spot.
       So, at index 0 we have a 1, and 1%5 is 1, so we replace the item at index 1 with 5 + that item.
       Now our array is [1,9,3,3,3].
       Next, at index 1 we have a 9, and 9%5 is 4 (adding 5 didn't change the fact that we can still find the original value with % 5),
        so we replace the item at index 4 with 5 + that item.
        Our array is now [1, 9, 3, 3, 8].
        Continuing, we get [1, 9, 3, 8, 8] then [1, 9, 3, 13, 8] and finally [1, 9, 3, 18, 8].
         When we iterate through to find the values at the end, starting at index 1,
         we find that 9/5 is greater than 1, 3/5 is not greater than 1, 13/5 and 8/5 are greater than 1.
         Thus, since 3/5 is the first not greater than 5, we know index 2 was never used or added to,
         so 2 is the missing number.

        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.append(0)
        # remove useless item
        for i in range(len(nums)):
            if nums[i] < 1 or nums[i] > n + 1:
                nums[i] = 0
        for i in range(len(nums)):
            nums[nums[i] % n] += n

        for i in range(len(nums)):
            if nums[i] / n < 1:
                return i + 1
        return n


if __name__ == "__main__":
    nums = [2, 1]
    Solution().firstMissingPositive(nums)
