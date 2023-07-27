# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == right:
            return head
        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for i in range(left-1):
            pre = pre.next
        
        # reverse
        cur = pre.next
        for i in range(right - left):
            # 3
            nxt = cur.next
            # 2 -> 4
            cur.next = cur.next.next
            # 1 -> 3, move to the front
            nxt.next = pre.next
            pre.next = nxt


        return dummyNode.next







