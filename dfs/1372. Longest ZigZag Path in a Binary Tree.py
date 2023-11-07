# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_path = 0
        @cache
        def helper(node, direction, path):
            nonlocal max_path
            if not node:
                return path
            if direction == 'left':
                left = helper(node.left, 'left', 0)
                right = helper(node.right, 'right', path+1)
                max_path = max(left, right, max_path)
            if direction == 'right':
                left = helper(node.left, 'left',path+1)
                right = helper(node.right, 'right', 0)
                max_path = max(left, right, max_path)
            return path

        helper(root.left, 'left', 0)
        helper(root.right, 'right', 0)

        return max_path