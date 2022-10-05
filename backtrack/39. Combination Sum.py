# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates
# where the chosen numbers sum to target. You may return the combinations in any order.
#
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.
#
# The test cases are generated such that the number of unique combinations
# that sum up to target is less than 150 combinations for the given input.

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def backtrack(candidates, comb, remain, res):
            if remain < 0:
                return
            if remain == 0:
                res.append(comb)
            for i in range(len(candidates)):
                if comb not in res:
                    backtrack(candidates[i:], comb + [candidates[i]], remain - candidates[i], res)

        res = []
        backtrack(candidates, [], target, res)
        return res