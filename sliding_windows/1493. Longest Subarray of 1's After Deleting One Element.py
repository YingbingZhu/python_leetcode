#
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        res = 0
        cnt = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                cnt += 1
            # shrink the window to make cnt <= 1
            while cnt > 1:
                if nums[l] == 0:
                    cnt -= 1
                l += 1
            res = max(res, r - l)
        return res

