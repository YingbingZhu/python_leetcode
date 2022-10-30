class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        larger = p = len(nums) - 1
        while p >= 1 and nums[p] <= nums[p - 1]:
            p -= 1
        if p == 0:
            nums.reverse()
            return
        while larger >= 0 and nums[larger] <= nums[p - 1]:
            larger -= 1
        nums[larger], nums[p - 1] = nums[p - 1], nums[larger]
        # reverse the remain
        l = p
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1



