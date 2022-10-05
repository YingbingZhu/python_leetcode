# Given an array nums of distinct integers,
# return all the possible permutations. You can return the answer in any order.

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(m, nums, perm, res):
            if len(perm) == m:
                res.append(perm)
                return
            for i in range(len(nums)):
                if perm not in res:
                    dfs(m, nums[:i] + nums[i + 1:], perm + [nums[i]], res)

        res = []
        dfs(len(nums), nums, [], res)

        return res