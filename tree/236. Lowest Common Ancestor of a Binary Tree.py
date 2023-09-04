# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root:None}
        stack = [root]
        while p not in parents or q not in parents:
            cur = stack.pop()
            if cur.left:
                stack.append(cur.left)
                parents[cur.left] = cur
            if cur.right:
                stack.append(cur.right)
                parents[cur.right] = cur

        anc = set()
        while p:
            anc.add(p)
            p = parents[p]
        
        while q not in anc:
            q = parents[q]
        
        return q
