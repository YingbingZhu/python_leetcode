# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        size, extra = divmod(length, k)
        res = []
        
        p = head
        prev = None
        for _ in range(k):
            sentinel = ListNode(0)
            sentinel.next = p
            for _ in range(size+(1 if extra> 0 else 0)):
                prev = p
                p = p.next
            res.append(sentinel.next)
            if prev:
                prev.next = None
            extra -= 1

        return res

        