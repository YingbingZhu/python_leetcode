class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if  len(nums) == 1 and nums[0] >= 1:
            return 1

        return len(set([num for num in nums if num != 0]))
        