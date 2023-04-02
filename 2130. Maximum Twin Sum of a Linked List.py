# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        mid = prev
        
        
        
        max_sum = 0
        
        while mid:
            max_sum = max(max_sum, head.val + mid.val)
            mid = mid.next
            head = head.next
        
        return max_sum
            
        
        
        
        
            
        
