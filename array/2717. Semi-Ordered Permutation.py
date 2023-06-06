class Solution(object):
    def semiOrderedPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        end = len(nums)
        res = 0
        meet = False
        for i, n in enumerate(nums):
            if n == 1:
                res += i
                meet = True
            if n == end:
                if meet:
                    res += n - i - 1
                else:
                    res += n - i - 2
        return res
