# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
#
# You should rearrange the elements of nums such that the modified array follows the given conditions:
#
# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # for i, n in enmerate(nums):
        #     if
        res = []
        insert = 0
        positive = negative = 0
        while insert < len(nums):
            while nums[positive] < 0:
                positive += 1
            while nums[negative] > 0:
                negative += 1
            res.append(nums[positive])
            res.append(nums[negative])
            positive += 1
            negative += 1
            insert += 2
        return res