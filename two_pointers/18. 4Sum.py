class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        for i in range(len(nums) - 3):
            if i == 0 or nums[i] != nums[i - 1]:
                for j in range(i + 1, len(nums) - 2):
                    l = j + 1
                    r = len(nums) - 1
                    while l < r:
                        curr = nums[i] + nums[j] + nums[l] + nums[r]
                        if curr < target:
                            l += 1
                        elif curr > target:
                            r -= 1
                        else:
                            tmp = [nums[i], nums[j], nums[l], nums[r]]
                            if tmp not in res:
                                res.append(tmp)
                            l += 1
                            r -= 1
        return res
