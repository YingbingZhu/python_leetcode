# You are given an array nums that consists of non-negative integers.
# Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21.
# A pair of indices (i, j) is nice if it satisfies all of the following conditions:
#
# 0 <= i < j < nums.length
# nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
# Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.


class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def rev(s):
            return int(str(s)[::-1])

        d = {}
        for num in nums:
            d[num - rev(num)] = d.get(num - rev(num), 0) + 1

        return sum(freq * (freq - 1)/2 for freq in d.values()) % (10 ** 9 + 7)
