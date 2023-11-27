# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':


        def check(node, nodes):
            if not node:
                return None
            if node in nodes:
                return node
            left = check(node.left, nodes)
            right = check(node.right, nodes)
            if left and right:
                return node
            if left:
                return left
            if right:
                return right
        
        return check(root, nodes)

