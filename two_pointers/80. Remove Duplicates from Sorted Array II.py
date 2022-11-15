class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = 2
        # future num to replace nums[s]
        for f in range(2, len(nums)):
            if nums[s - 2] != nums[f]:
                nums[s] = nums[f]
                s += 1
        return s
