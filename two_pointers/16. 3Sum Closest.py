#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/10/8
"""


# Given an integer array nums of length n and an integer target,
# find three integers in nums such that the sum is closest to target.
#
# Return the sum of the three integers.
#
# You may assume that each input would have exactly one solution.


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = nums[0] + nums[1] + nums[-1]
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                curr_sum = nums[l] + nums[r] + nums[i]
                if abs(curr_sum - target) < abs(ans - target):
                    ans = curr_sum
                if curr_sum == target:
                    return ans
                elif curr_sum - target > 0:
                    r -= 1
                else:
                    l += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [4, 0, 5, -5, 3, 3, 0, -4, -5]
    target = -2
    curr_sum = s.threeSumClosest(nums, target)
    print(curr_sum)
