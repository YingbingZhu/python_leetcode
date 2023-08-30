"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        mapping = {}
        p = head
        while p:
            node = Node(p.val)
            mapping[p] = node
            p = p.next
        
        p = head
        while p:
            if p.next:
                mapping[p].next = mapping[p.next]
            if p.random:
                mapping[p].random = mapping[p.random]    
            p = p.next

        return mapping[head]   