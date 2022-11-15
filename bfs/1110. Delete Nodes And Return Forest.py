# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        res = []
        # root, has parent
        queue = deque([(root, False)])
        while queue:
            for _ in range(len(queue)):
                node, hasParent = queue.popleft()
                if not hasParent and node.val not in to_delete:
                    res.append(node)
                hasParent = not node.val in to_delete

                if node.left:
                    queue.append((node.left, hasParent))
                    if node.left.val in to_delete:
                        node.left = None

                if node.right:
                    queue.append((node.right, hasParent))
                    if node.right.val in to_delete:
                        node.right = None

        return res
