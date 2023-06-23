class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        # i - j
        for i, v1 in enumerate(nums[1:], start=1):
            for j, v2 in enumerate(nums[:i]):
                delta = v1 - v2
                if (j, delta) in dp:
                    dp[i, delta] = dp[j, delta] + 1
                else:
                    dp[i, delta] = 2
        return max(dp.values())