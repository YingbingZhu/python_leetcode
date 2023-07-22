class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1] * n
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        count[i] = 0
                    if dp[i] == dp[j] + 1:
                        count[i] += count[j] 
        res = 0
        max_length = max(dp)

        for i in range(n):
            if dp[i] == max_length:
                res += count[i]
        return res