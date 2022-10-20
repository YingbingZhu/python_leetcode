# You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.
#
# For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.
#
# Return the head of the modified linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        p1 = head
        p2 = head.next
        while p2:
            curr = 0
            while p2 and p2.val!=0:
                curr += p2.val
                p2 = p2.next
            p1.next.val = curr
            p1 = p1.next
            p2 = p2.next
        p1.next = None
        return head.next