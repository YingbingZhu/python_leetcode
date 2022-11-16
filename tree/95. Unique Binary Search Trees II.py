#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/16
"""
# Given an integer n, return all the structurally unique BST's (binary search trees),'
#  which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.helper(1, n)

    def helper(self, start, end):
        if start > end:
            return [None]

        trees = []
        for root_val in range(start, end+1):
            left_subtrees = self.helper(start, root_val-1)
            right_subtrees = self.helper(root_val+1, end)
            for left in left_subtrees:
                for right in right_subtrees:
                    curr_root = TreeNode(root_val)
                    curr_root.left = left
                    curr_root.right = right

                    trees.append(curr_root)
        return trees
