class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = twos = 0
        for num in nums:
            # toggle bits appear once and remove bits appear twice
            ones = (ones ^ num) & ~twos
            # toggle bits appear twice and remove bits appear once
            twos = (twos ^ num) & ~ones
        return ones