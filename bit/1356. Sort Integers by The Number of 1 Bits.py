class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        return sorted(arr, key=lambda x : (self.hamming_weights(x), x))

    def hamming_weights(self, num):
        weight = 0
        while num:
            weight += 1
            num &= num - 1  # remove rightmost 1
        return weight