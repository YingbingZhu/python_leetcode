# You are given a 0-indexed array nums consisting of n positive integers.
#
# The array nums is called alternating if:
#
# nums[i - 2] == nums[i], where 2 <= i <= n - 1.
# nums[i - 1] != nums[i], where 1 <= i <= n - 1.
# In one operation, you can choose an index i and change nums[i] into any positive integer.
#
# Return the minimum number of operations required to make the array alternating.


class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        odd = {}
        even = {}
        for i in range(len(nums)):
            if i % 2 != 0:
                odd[nums[i]] = odd.get(nums[i], 0) + 1
            else:
                even[nums[i]] = even.get(nums[i], 0) + 1

        top = second = (None, 0)
        for k, v in odd.items():
            if v > top[1]:
                top, second = (k, v), top
            elif v > second[1]:
                second = (k, v)

        topE = secondE = (None, 0)
        for k, v in even.items():
            if v > topE[1]:
                topE, secondE = (k, v), topE
            elif v > secondE[1]:
                secondE = (k, v)
        if top[0] != topE[0]:
            return len(nums) - top[1] - topE[1]
        else:
            return len(nums) - max(top[1] + secondE[1], topE[1] + second[1])
