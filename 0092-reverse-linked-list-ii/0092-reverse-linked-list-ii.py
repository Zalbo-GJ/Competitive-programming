# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        
        curr = head
        non_reverse_last = None
        
        for i in range(left-1):
            non_reverse_last = curr
            curr = curr.next
            
        reverse_last = curr
        
        prev = nxt = None
        i = 0
        while curr and i < right-left+1:
            
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
            i += 1
        
        if non_reverse_last:
            non_reverse_last.next = prev
        else:
            head = prev
        
        reverse_last.next = curr
        
        return head
        