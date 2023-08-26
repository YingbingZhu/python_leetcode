# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        new = ListNode(0)
        p = new
        carry = 0
        while p1 or p2:
            p1_val = p1.val if p1 else 0 
            p2_val = p2.val if p2 else 0
            cur = p1_val + p2_val + carry
            carry, cur = divmod(cur, 10)
            node = ListNode(cur)
            p.next = node
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            p = p.next
        if carry>0:
            p.next = ListNode(carry)
        return new.next
