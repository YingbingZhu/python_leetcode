class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] == val and nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
            elif nums[l] == val and nums[r] == val:
                r -= 1
            else:
                l += 1
        return l