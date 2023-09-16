#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/17
"""
from functools import lru_cache


# Given an array of distinct integers nums and a target integer target,
# return the number of possible combinations that add up to target.
#
# The test cases are generated so that the answer can fit in a 32-bit integer.
# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def backtrack(remain, dp):
            if remain < 0:
                return 0
            elif remain == 0:
                return 1
            elif remain in dp:
                return dp[remain]

            count = 0
            for i in range(len(nums)):
                count += backtrack(remain - nums[i], dp)
            dp[remain] = count
            return count

        res = backtrack(target, {})
        print(res)
        return res

    # @lru_cache(sum(nums))
    # def backtrack(remain):
    #     if remain == 0:
    #         return 1
    #     elif remain < 0:
    #         return 0s
    #     cnt = 0
    #     for i in range(len(nums)):
    #         remain -= nums[i]
    #         cnt += backtrack(remain)
    #         remain += nums[i]
    #     return cnt
    #
    # return backtrack(target)


if __name__ == "__main__":
    s = Solution()
    s.combinationSum4(nums=[4, 2, 1], target=32)
