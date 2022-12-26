#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/26
"""
# You are given an integer array nums. You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_pos = 0
        index = 0
        while index <= max_pos:
            max_pos = max(max_pos, index + nums[index])
            if max_pos >= len(nums) - 1:
                return True
            index += 1
        return False


if __name__ == '__main__':
    Solution().canJump(nums=[2,3,1,1,4])
        