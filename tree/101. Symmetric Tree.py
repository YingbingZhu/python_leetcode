# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(a, b):
            if not a and not b:
                return True
            if not a and b:
                return False
            if not b and a:
                return False
            if a.val == b.val:
                return check(a.left, b.right) and check(a.right, b.left)
        return check(root.left, root.right)
            