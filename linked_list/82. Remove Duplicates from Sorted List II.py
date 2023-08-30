# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # the slow pointer link up the unique listnodes
        slow = dummy
        fast = head
        while fast and fast.next:
            while fast.next and fast.val == fast.next.val:
                fast = fast.next
            if slow.next == fast:
                slow = slow.next
            else:
                slow.next = fast.next
            fast = fast.next
        return dummy.next