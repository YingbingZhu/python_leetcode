# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        index = 0
        start = list1
        while index < a - 1:
            index += 1
            start = start.next
        end = start
        while index <= b:
            index += 1
            end = end.next
        start.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = end
        return list1