class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def can_pair(mid):
            count = 0
            i = 0
            while i < len(nums) - 1 and count < p:
                if nums[i+1] - nums[i] <= mid:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= p
        
        nums.sort()
        l = 0
        r = nums[-1] - nums[0]

        while l < r:
            mid = (l+r) // 2
            if can_pair(mid):
                r = mid
            else:
                l = mid + 1
        return l