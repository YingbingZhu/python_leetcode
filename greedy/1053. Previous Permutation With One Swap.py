# Given an array of positive integers arr (not necessarily distinct),
# return the lexicographically largest permutation that is smaller than arr,
# that can be made with exactly one swap (A swap exchanges the positions of two numbers arr[i] and arr[j]).
# If it cannot be done, then return the same array.

class Solution(object):
    def prevPermOpt1(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
