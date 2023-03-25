# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head and head.next:
            
            nxt = head.next
            head.next = self.swapPairs(nxt.next)
            nxt.next = head
            
            return nxt
        
        return head