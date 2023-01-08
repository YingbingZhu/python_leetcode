from math import ceil


class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        score = 0
        i = 0
        max_value = nums[0]
        while k > 0 and i < len(nums):
            if nums[i] > max_value:
                max_value = nums[i]

            score += nums[i]
            nums[i] = ceil(nums[i] / 3)
            k -= 1
        return score


if __name__ == '__main__':
    nums = [756902131,995414896,95906472,149914376,387433380,848985151]
    k = 6
    Solution().maxKelements(nums, k)