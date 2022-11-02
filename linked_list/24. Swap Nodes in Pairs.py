# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without
# modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tmp = head.next
        prev = ListNode(0)
        first = head
        while first and first.next:
            second = first.next
            first.next = second.next
            prev.next = second
            second.next = first
            prev = first
            first = first.next
        return tmp