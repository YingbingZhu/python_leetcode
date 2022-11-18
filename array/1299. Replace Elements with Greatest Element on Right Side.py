#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/18
"""


# Given an array arr, replace every element in that array with the greatest element among the elements to its right,
# and replace the last element with -1.
#
# After doing so, return the array.


class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        curr = -1
        for i in range(len(arr)-1, -1, -1):
            tmp = arr[i]
            arr[i] = curr
            if tmp > curr:
                curr = tmp
        return arr


if __name__ == "__main__":
    s = Solution()
    arr = [17, 18, 5, 4, 6, 1]
    s.replaceElements(arr)
