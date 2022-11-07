# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        x = head
        # Check if we need to reverse the group
        for i in range(k):
            if not x:
                return head
            x = x.next
        
        # Reverse the group (basic way to reverse linked list)
        prev,curr= None, head
        for i in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
             # After reverse, we know that `head` is the tail of the group.
		# And `curr` is the next pointer in original linked list order
        head.next = self.reverseKGroup(curr, k)
        
        return prev