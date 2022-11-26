# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        before = ListNode(0)
        after = ListNode(0)
        bp = before
        ap = after

        p = head
        while p:
            if p.val < x:
                bp.next = p
                bp = bp.next
            else:
                ap.next = p
                ap = ap.next
            p = p.next

        ap.next = None
        bp.next = after.next

        return before.next