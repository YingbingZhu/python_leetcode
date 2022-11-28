#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/25
"""


# Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr.
# Since the answer may be large, return the answer modulo 109 + 7.


class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        stack = []
        for i in range(len(arr) + 1):
            # when reach the end
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                prev = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i
                # combinations
                count = (prev - left) * (right - prev)
                res += (count * arr[prev])
            # if new element is bigger, then append
            stack.append(i)
        return res % (10 ** 9 + 7)


if __name__ == "__main__":
    s = Solution()
    arr = [3, 1, 2, 4]
    s.sumSubarrayMins(arr)
