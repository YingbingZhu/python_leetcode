#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/11
"""
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place
# such that each unique element appears only once. The relative order of the elements should be kept the same.
#
# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = j = 0
        while j < len(nums):
            while j < len(nums)-1 and nums[j] == nums[j+1]:
                j += 1
            nums[i] = nums[j]
            i += 1
            j += 1
        return i


if __name__ == "__main__":
    s = Solution()
    s.removeDuplicates([1, 1, 2, 2, 2, 3])