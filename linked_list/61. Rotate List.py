# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return head
        length = 1
        prev = head
        while prev.next:
            prev = prev.next
            length += 1

        if not length or not k % length:
            return head

        p = head
        for _ in range(length - k % length - 1):
            p = p.next

        newHead = p.next
        p.next = None
        prev.next = head
        return newHead


