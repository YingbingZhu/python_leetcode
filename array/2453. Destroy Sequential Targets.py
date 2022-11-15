class Solution(object):
    def destroyTargets(self, nums, space):
        """
        :type nums: List[int]
        :type space: int
        :rtype: int
        """
        nums.sort()
        freqs = {}
        mi = float('inf')
        for num in nums:
            freqs[num % space] = freqs.get(num % space, 0) + 1
        max_freq = max(freqs.values())
        for num in nums:
            if freqs[num % space] == max_freq and num < mi:
                mi = num
        return mi
