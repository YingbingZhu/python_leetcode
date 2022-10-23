# You are given the head of a linked list containing unique integer values and an integer array nums
# that is a subset of the linked list values.
#
# Return the number of connected components in nums
# where two values are connected if they appear consecutively in the linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: ListNode
        :type nums: List[int]
        :rtype: int
        """
        p = head
        s = set(nums)
        res = 0
        while p:
            if p.val in s and (not p.next or p.next.val not in s):
                res += 1
            p = p.next
        return res
