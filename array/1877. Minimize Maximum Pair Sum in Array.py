class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        mid = n // 2
        ans = nums[0] + nums[-1]
        for i in range(mid):
            ans = max(ans, nums[i] + nums[n - i - 1])
        return ans
        