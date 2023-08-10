class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        while l <= r:
            # avoid duplicates
            while l < r and nums[r] == nums[r - 1]:
                r -= 1
            while l < r and nums[l] == nums[l + 1]:
                l += 1

            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            # mid in left side
            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False






