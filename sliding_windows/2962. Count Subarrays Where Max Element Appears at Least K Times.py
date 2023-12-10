class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        target = max(nums)
        ans = 0
        n = len(nums)
        cnt = 0
        l = r = 0
        while r < n:
            if nums[r] == target:
                cnt += 1
            
            while cnt >= k:
                ans += len(nums) - r 
                if nums[l] == target:
                    cnt -= 1
                l += 1
            r += 1
        return ans
            
        