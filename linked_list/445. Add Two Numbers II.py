# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        total = 0
        carry = 1
        res_l = ListNode()
        while s1 or s2:
            if s1:
                total += s1.pop()
            if s2:
                total += s2.pop()
            digit = total % 10
            carry = total // 10
            res_l.val = digit
            head = ListNode(carry)
            head.next = res_l
            # move pointer ahead
            res_l = head
            total = carry
        return res_l.next if carry == 0 else res_l
                     