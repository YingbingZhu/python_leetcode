from collections import defaultdict


class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        i = 0
        count = 0
        d = defaultdict(int)
        for j in range(len(nums)):
            count += d[nums[j]]
            d[nums[j]] += 1
            while count >= k:
                d[nums[i]] -= 1
                count -= d[nums[i]]
                i += 1
            res += i
        return res