class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            curr = nums[i]
            while res and res[-1] > curr and len(nums)-i+len(res)>k:
                res.pop()
            if len(res) < k:
                res.append(curr)
        return res