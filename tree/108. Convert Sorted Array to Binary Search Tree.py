#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/2
"""


# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def makeBST(nums, start, end):
            if start >= end:
                return None
            return TreeNode(
                val=nums[(start + end) // 2],
                left=makeBST(nums, start, (start + end) // 2),
                right=makeBST(nums, (start + end) // 2+1, end)
            )

        return makeBST(nums, 0, len(nums))