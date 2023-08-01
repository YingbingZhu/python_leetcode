class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        l = r = 0
        max_pos = nums[0]
        while r < len(nums) - 1:
            ans += 1
            for i in range(l, r+1):
                if i + nums[i] >= len(nums) - 1:
                    return ans
                max_pos = max(max_pos, i+nums[i])
            l = r + 1
            r = max_pos
        return ans