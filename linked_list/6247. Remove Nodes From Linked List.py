# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new = ListNode(0)
        tmp = new
        p = head
        while p:
            fast = p.next
            while fast:
                if fast.val <= p:
                    fast = fast.next
                else:
                    p = p.next
            new.next = p
            new = new.next
            p = p.next
        return tmp.next

