"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return root
        q = deque([root])
        sentinel = Node(0)

        while q:
            prev = sentinel
            for _ in range(len(q)):
                cur = q.popleft()
                level = []
                if cur.left:
                    q.append(cur.left)
                    prev.next = cur.left
                    prev = prev.next
                if cur.right:
                    q.append(cur.right)
                    prev.next = cur.right
                    prev = prev.next
        return root