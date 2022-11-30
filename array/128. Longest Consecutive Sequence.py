#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/30
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = 1
        seen = set(nums)
        for num in seen:
            if num - 1 not in seen:
                start = num
                cons = 1

                while start + 1 in seen:
                    start += 1
                    cons += 1
                    res = max(cons, res)

        return res


if __name__ == "__main__":
    s = Solution()
    nums = [0, 4, 1, 3, 2, 5]
    s.longestConsecutive(nums)
