# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1=p2=head
        for i in range(n):
            p2 = p2.next
        if not p2:
            return head.next
        
        while p2 and p2.next:
            p1= p1.next
            p2= p2.next
        
        p1.next = p1.next.next
        
        return head