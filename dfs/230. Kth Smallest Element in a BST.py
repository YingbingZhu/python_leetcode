# Given the root of a binary search tree, and an integer k,
# return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Definition for a binary tree node.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        path = []
        self.inOrder(root, path)
        return path[k - 1]

    def inOrder(self, root, path):
        if not root:
            return
        if root.left:
            self.inOrder(root.left, path)
        path.append(root.val)
        if root.right:
            self.inOrder(root.right, path)