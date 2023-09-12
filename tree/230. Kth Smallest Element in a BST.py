# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        cnt = 0
        def inOrder(node):
            nonlocal cnt, res
            if not node:
                return
            inOrder(node.left)
            cnt += 1
            if k == cnt:
                res = node.val
                return
            inOrder(node.right)
        
        res = 0
        inOrder(root)
        return res