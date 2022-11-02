#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/10/25
"""
# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head.next
        while fast:
            slow, fast = fast, slow
            fast = fast.next.next
            slow = slow.next
        return head

